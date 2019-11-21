# 手机抖音app无水印视频下载

### 禁止恶意使用，仅交流学习！

## 环境

	* PYTHON
	* charles抓包软件
	* requests库
	* jsonpath库
	* time库
	* re库

## 实现思路

* charles抓包，抓接口
* 获取sec_user_id，max_cursor信息，url构造
* 反爬处理

## 函数说明

* get_uid()                     获取sec_user_id参数
* get_videourl()            获取视频无水印下载链接
* down()                         下载视频到本地        

## 文件结构

	* douyi.py是代码文件
	* video文件夹存放下载的视频（这里只放了几个图）

## 闲聊几句

在用charles抓包的时候，虽然能拿到链接，但是无论怎么构造都返回空信息，很难受有木有。后来发现是有个_signature这个参数，啧啧啧，立马浏览器断点一波操作。结果发现，孩子醒醒你对这个不熟.....就放弃啦（其实有努力挣扎了好久）。

目前我找到的这个是可以爬个人喜欢的视频的，别的一堆也没怎么搞，有空再搞吧。

使用的话就复制分享链接就好了。

#### 示范操作

 * 打开抖音app选择你喜欢的人的主页
   ![1.png](https://i.loli.net/2019/11/21/U9kDtFVOWmRw2Ad.png)
   
 * 点击
![2.png](https://i.loli.net/2019/11/21/vxlgsWh9dfkHpXL.png) 
 * 	复制链接
![3.png](https://i.loli.net/2019/11/21/HyzQN82qAj7DLU9.png)
* 运行程序，将链接复制进去
![5.png](https://i.loli.net/2019/11/21/liUrKgJa1wnGCOH.png)





