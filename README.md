# 相关代码已经修改调试成功----2017-4-1  #
## **一、说明** ##

**1.目标网址：**[http://www.cgris.net/query/croplist.php](http://www.cgris.net/query/croplist.php)

**2.实现：爬取相关信息如图所示，爬取的数据存入mysql数据库。**

**3.结果数据存放百度云：** 链接：[http://pan.baidu.com/s/1jHKv6Cm](http://pan.baidu.com/s/1jHKv6Cm) 密码：mlp2 （数据是sql，要放在mysql中运行即可）

图1
![](http://images2015.cnblogs.com/blog/1129740/201704/1129740-20170401102108727-998626880.png)

图2
![](http://images2015.cnblogs.com/blog/1129740/201704/1129740-20170401102120195-1133290644.png)
数据结果部分截图：

图3

![](http://images2015.cnblogs.com/blog/1129740/201704/1129740-20170401102654508-569931415.png)


## **二、运行** ##
1. 程序运行前先要配置相应的数据库参数；
2. 然后修改我在程序中有注释的参数；
3. 最后运行程序即可，查看mysql中是否有数据。

## **三、问题**----欢迎留言提出问题##
声明：此处的问题对本项目（公司要求）影响不大,由于本人时间有限，只要能尽快的获得数据即可
> 1. 项目中小类比较多，所以修改参数的次数比较多，比较烦（待解决）————————**志同道合的朋友可以改进代码**；
> 2. 本项目没有找到js包，所以只能用selenium，模拟鼠标点击，要等待加载完全，效率比较低。在点击下一页的过程中会碰到数据不变的情况，虽然我有去重功能，但是会导致数据丢失【1000条数据里面少60条，还可以】（待解决）。
> 3. 代码中webdriver.Chrome()用谷歌，用Fire或者是别的浏览器会导致总数变少，如上图2只有13944个，其实应该有22058个，不知道是什么原因，可能是不兼容吧，不得不佩服还是谷歌强大（待解决）————————不信的朋友可以亲自尝试。

**欢迎有兴趣的小伙伴帮我优化，找出问题，之后我将合并你的代码，作为贡献者,共同成长。**

## **四、笔记** ##
难点：

> 1.源代码没有相关数据，没有找到js包，抓不到包。

散点知识：

>  1. 这是我第一次使用selenium模拟鼠标点击，是一个很神奇的东西。
>  2. from selenium import webdriver相关知识点，虫师博客关于selenium写得还不错，汇总。[selenium学习传送门](http://www.cnblogs.com/fnng/p/3157639.html)，《Selenium 2自动化测试实战 基于Python语言》有空我要买下这本书。
>  3. selenium基本用法

	    #-*- coding:utf-8 -*-
	    from selenium import webdriver
	    url='http://www.cgris.net/query/do.php#其它作物,橡胶'
	    browser = webdriver.Chrome() #打开谷歌浏览器
	    browser.get(url)  #打开网页
	    browser.implicitly_wait(3) #等待加载完全
	    browser.find_element_by_css_selector('div[onclick="query()"]').click() #鼠标所做的事情
	    browser.implicitly_wait(2)
	    browser.find_element_by_id('nexthehe').click()

----------
如果本项目对你有用请给我一颗star，万分感谢。