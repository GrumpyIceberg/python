# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 16:51:20 2018

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 09:10:48 2018
K12（小学到高中12年的简称）--
高考--高考派(统计全中国大学招生情况，例如北京大学(3000)在北京招多少人？在重庆？在全国？)
全中国有多少所大学？
全中国有多少个城市？
在某个城市文科招的人数？理科招生的人数？
====
全国大学招生人数排行：例如
郑州大学 8000
桂林大学 6000
.....
西藏藏医学院：5
=
家长帮班级项目：
注意点：同一时间，访问量过大，可能会导致本次项目无法进行，因为北京那边服务器奔溃。导致全国都无法访问。
导致对方程序员加班。所以我们整个班级，需要有一套策略，要拿到所有数据但不会导致奔溃。
策略例如：
======
题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""

import urllib.request as r
f=open('./all_school.txt','r',encoding='utf-8')
data=f.read()
import re
ls1=re.compile('daxue-jianjie-(.*?).html',re.S).findall(data)
print(ls1)
f.close


req=r.Request('http://www.gaokaopai.com/daxue-zhaosheng-477.html',headers={"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'})
date=r.urlopen(req).read().decode('utf-8')
ls=re.compile('unclaimCi.*?, (.*?)">(.*?)</li>',re.S).findall(date)
for i in range(len(ls)):
    print('城市为{},编号为{}'.format(ls[i][1],ls[i][0]).replace(')',''))
    #f.write('{},{}'.format(ls[i][1],ls[i][0]).replace(')','')

url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
f=open('./江西文科.txt','w',encoding='utf-8')
for i in ls1:
    data='id={}&type=1&city=36&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    if d.startswith('<!DOCTYPE html>'):
        print('编号{}存在错误'.format(i))
        while True:
            data='id={}&type=1&city=36&state=1'.format(i).encode()
            req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
            d=r.urlopen(req).read().decode('utf-8','ignore')
            if d.startswith('{'):
                f.write(d+'\n')
                break
    f.write(d+'\n')





f=open('./江西文科.txt','r',encoding='utf-8')
da=f.read()
ls2=re.compile('"plan":"(.*?)","uniname"',re.S).findall(da)
f.close
n=0
for w in range(len(ls2)):
    n=n+int(ls2[w])
print('江西文科招生人数为{}'.format(n))


    


    