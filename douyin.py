from selenium import webdriver
import jsonpath
import requests
import os
import re
import time
from multiprocessing.dummy import Pool

share_url = '' 
n = 0
name = 0
s = requests.Session()
video_li = []

share_url = input('请输入分享的链接：')   
#这个是下载的请求头
# headers_v = {
#     'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36',
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# }

#这个是拿视频链接的请求头
headers_li = {
    'Host': 'www.iesdouyin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Connection': 'keep-alive'
}

#获取uid，dkty，tac等参数
def get_data():
    global share_url
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver  =webdriver.Chrome('chromedriver.exe')#无头,chrome_options=options) #无头算出来的值有误，所以关啦
    driver.get(share_url)

    re_url = driver.current_url   #从跳转的url里拿sec_uid
    sec_uid = re.search(r'sec_uid=(.*?)&' , re_url).group(1)
    html = driver.page_source
    tac = re.search(r"tac='(.*?)'" , html).group(0)
    uid = re.search(r'uid: "(.*?)"' , html).group(1)
    dytk = re.search(r"dytk: '(.*?)'" , html).group(1)

    with open('page.html' , 'r') as f:
        page = f.read()
    with open('get_s.html' , 'w') as f:
        new_page = page.replace("tac='***'" , tac).replace('****' , uid)
        f.write(new_page)
    driver.get('file:///'+os.path.abspath('get_s.html'))
    signature = re.search(r'</script>(.*?)</body>' , driver.page_source ).group(1)
    driver.close()
    get_videourl( sec_uid , signature , dytk)
    

#获取视频下载链接
def get_videourl(sec_uid  , signature , dytk):
    global n
    url = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?sec_uid={}&count=21&max_cursor={}&aid=1128&_signature={}&dytk={}'
    new_u = url.format(sec_uid , n , signature , dytk)
    html = s.get( new_u, headers = headers_li)
    for i in range(len(html.json()['aweme_list'])):
        try:
            url_li = jsonpath.jsonpath(html.json() , 'aweme_list.{}.video.play_addr.url_list'.format(i))[0][0]
            n = jsonpath.jsonpath(html.json(), 'max_cursor')[0]
            print(url_li)
        except:
            #人生总会有这样那样的意外，跳过就好，哈哈哈哈。
            pass        
        #保存视频链接
        video_li.append(url_li)
        
        # get_data()
    #判断是否还有下一页  
    if jsonpath.jsonpath(html.json(), 'has_more')[0] :
        get_videourl( sec_uid , signature , dytk)

#视频下载
def down(v_url):
    #下载代码删了，但是请求头（headers_v）还留着，下载代码不难
    pass

def start():
    # 多线程下载
    pool = Pool(5)
    pool.map(down , video_li)


if __name__=='__main__':
    get_data()
    # start()
    
    