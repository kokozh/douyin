import requests
import jsonpath
import time
import re

n = 0
s = requests.Session()

def get_uid(url):
    headers = {
    'Host': 'v.douyin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Cookie': '_ga=GA1.2.854633755.1574303077; _gid=GA1.2.2076801614.1574303077',
    'Upgrade-Insecure-Requests': '1',
}
    html = s.get(url , headers = headers ,allow_redirects=False) #禁止自动重定向
    # print(html.headers['location'])
    return re.search(r'sec_uid=(.*?)&' , html.headers['location']).group(1)

def get_videourl(url , uid):
    global n
    new_url = url.format(n , uid)
    print(new_url)
    html = s.get(new_url)
    for i in range(len(html.json()['aweme_list'])):
        try:
            url_li = jsonpath.jsonpath(html.json() , 'aweme_list.{}.video.play_addr.url_list'.format(i))[0][0]
            try:
                name = jsonpath.jsonpath(html.json() , 'aweme_list.{}.desc')[0]
            except:
                name = "{}-{}".format(n , i)
        except:
            pass
        down(url_li,name)
        time.sleep(2)
    n = jsonpath.jsonpath(html.json(), 'max_cursor')[0]
    if jsonpath.jsonpath(html.json(), 'has_more')[0] == 1:
        get_videourl(url , uid)

def down(url , name):
    video = requests.get(url).content
    # print(url_list)
    with open('./video/{}.mp4'.format(name) , 'wb') as f:
        f.write(video)
    print("name")



if __name__=="__main__":
    url = input('请输入分享的链接：')
    url2= 'https://aweme-lq.snssdk.com/aweme/v1/aweme/favorite/?max_cursor={}&sec_user_id={}&count=10&retry_type=no_retry&iid=93096754929&device_id=69998893110&ac=wifi&channel=tianzhuo_dy_dsg&aid=1128&app_name=aweme&version_code=870&version_name=8.7.0&device_platform=android'
    uid = get_uid(url)
    get_videourl(url2 , uid)
