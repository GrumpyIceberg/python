# python# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:17:21 2018
题目十七：软件发布会
软件发布地址之一：http://www.91xiazai.com/Publish/index
icon图片下载：https://www.easyicon.net/12740-color_colour_icon.html
http://www.zuiben.com/lib/upload.php
-----
1.图片名称，图标，软件下载地址，源代码下载地址，应用截图
2.分享朋友圈()
3.周一 软件发布会
    PPT 3页-朋友圈截图-展示，组员任务介绍，应用的用途....
===‘上课了’
15:20之前确定您的应用
今天-6/30开发应用分享朋友圈
7/2下午之前 9组软件发布(分享朋友圈)。
    
7/2下午 开始
    13:50-从第一组开始。拍照，短视频
@author: Administrator
"""
for i in range(2):
     print("{}{}{}{}".format(6*' ',9*'*',12*' ',9*'*'))
for i in range(2):
     print("{}{}{}{}".format(8*' ',1*'开心悦读',14*' ',1*'开心悦读'))
for i in range(2):
     print("{}{}".format(18*' ',1*'开心悦读'))
for i in range(2):
    print("{}{}{}{}".format(i*' ',i*'开心悦读',(31-i)*' ',i*'开心悦读'))
    print("{}{}{}{}".format(i*' ',i*'开心悦读',(31-i)*' ',i*'开心悦读'))
for i in range(1):
    print("{}{}{}{}".format(3*' ',1*'开心悦读',(27-i)*' ',1*'开心悦读'))
for i in range(1):
    print("{}{}".format(6*' ',(5-i)*'开心悦读'))
for i in range(1):
    print("{}{}".format((12-i)*' ',(3-i)*'开心悦读'))














##加载各种包，定义函数
import urllib.request as r
import re
##定义小说类型
y={'玄幻':'xuanhuan','修真':'xiuzhen','都市':'dushi','历史':'lishi','网游':'wangyou','科幻':'kehuan','恐怖':'kongbu','全本':'quanben'}
print('小说类型:')
for i in y:
    print('{}'.format(i))
##输入小说类型，获得此类型的100部小说推荐供读者选择
while True:
    a=input('请输入你想看的小说类型:')
    if a in y:
        url1=('http://www.biquge.com.tw/{}/'.format(y[a]))
        data=r.urlopen(url1).read().decode('gbk')
        shu=re.compile('<li><span class.*?href.*?">(.*?)<',re.S).findall(data)
        print('好看的{}小说推荐列表:')
        for i in range(len(shu)):
            print('{}:{}'.format(i,shu[i]))
        break
    else:
        print('提示:您的输入有误,请重新输入')
        continue
##根据小说列表选择自己想看的小说名，输入小说名，取得小说名地址shuid
while True:
    x=input('请输入你想看的小说名：')
    if x in shu:
        url2=('http://www.biquge.com.tw/{}/'.format(y[a]))
        data1=r.urlopen(url2).read().decode('gbk')
        shuid=re.compile('<li><span class.*?href="(.*?)".*?>{}<'.format(x)).findall(data1)
        break
    else:
        print('提示:您的输入有误,请重新输入')
        continue
##根据小说名地址，爬取章节page供读者选择
url3=shuid[0]
data2=r.urlopen(url3).read().decode('gbk')
page=re.compile('<dd><a href="/.*?/(.*?)">(.*?)<',re.S).findall(data2)
print('以下显示所有章节')
page2=[]
for i in range(len(page)):
    print('章节:{}'.format(page[i][1]))
    page2.append(page[i][1])
##用户选择阅读方式并开始阅读
while True:
    h=input('如需结束请输入"结束程序",如需查看章节请输入"查看章节",如需继续阅读请输入章节名:')
    if h in page2:
        for s in range(len(page)):
            if page[s][1]==h:
                url4='{}{}'.format(url3,page[s][0])
                data3=r.urlopen(url4).read().decode('gbk')
                read=re.compile('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',re.S).findall(data3)
                print('章节内容：')
                print(page[s][1])
                for i in range(len(read)):
                    print('    {}'.format(read[i]))
        continue
    if h=='查看章节':
        for i in range(len(page)):
            print('章节:{}'.format(page[i][1]))
        continue
    if h=='结束程序':
        print('程序结束-------------------')
        break
    else:
        print('提示:您的输入有误,请重新输入')
        continue
      
    













