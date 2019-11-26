

# 抖音无水印视频下载

## 环境

	* PYTHON
	* selenium库
	* multiprocessing库
	* time库
	* jsonpath库
	* re库
	* os库
	* Chrome浏览器（版本 78.0.3904.108）
## 实现方法

* 复制分享链接到浏览器，XHR分析一波，很明显这个就是我们要的。
* ![](https://i.loli.net/2019/11/25/xUySz1MuJcr2B3V.png)

* 看一下链接和请求参数，分析后发现sec_uid、max_cursor、_signature、dytk是我们要找的。简单的那些就不多说了，我们发现 _signature是算法生成的，那就去找吧。
* ![2.png](https://i.loli.net/2019/11/25/Xi1xBwIDckruPfa.png)
* ![3.png](https://i.loli.net/2019/11/25/UeZqpAKgfM2xOJc.png)
* 先来全局搜索，找一下_signature在哪里。
* ![4.png](https://i.loli.net/2019/11/25/kPrQ14fanpTMGCd.png)
* 哦豁，九曲十八弯呀！那就继续找喽
* ![5.png](https://i.loli.net/2019/11/25/ghSZPz9sXenD3Im.png)
* ![6.png](https://i.loli.net/2019/11/25/ZwKGxlXd3b4gSTO.png)
* 找到这里我们发现，它是require返回的，那继续看看这是个什么东西喽
* ![7.png](https://i.loli.net/2019/11/25/HVbGCTadkeRqU8g.png)
* 看到这里，大概心里已经有谱了。我这里没有仿照它加密过程写，我是直接将它的算法弄过来，写到html文件调用的。（断点调试比我上面这样找更快哦，我这样之是为了让你们理解得更清楚点而已。）

## 函数说明

* get_data（）                  获取uid、dytk、tac、signature等参数
* get_videourl（）            获取视频下载链接
* down（）                         视频下载  （这里将下载的代码给清空了，想下载请求头模拟成手机自己写哈）

## 文件结构

* video存放下载的无水印视频
* douyin.py是主程序
* page.html和get_s.html分别是_signature的算法页面和拼接了tac的算法页面

## 闲聊

* 有空用类重写一遍，现在就当做是学习啦。
* 运行程序报错的话估计是你的chrome浏览器和我的不一样哦，因为我selenium的chrome驱动用的是（适合chrome版本 78.0.3904.108）的。