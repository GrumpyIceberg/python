# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 14:12:06 2018

=====================一定要注意文件格式，保存的时候为utf-8
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序

@author: Administrator
"""
print('火车站三字码是：'+'BJX')

"""
    ls=open('./火车站编码.csv','r').readlines()
UnicodeDecodeError: 'gbk' codec can't decode byte 0xf8 in position 6572: illegal multibyte sequence
"""
def hanzi_to_pin(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入年月日：')
from_station=input('出发站：')
from_station=hanzi_to_pin(from_station)
to_station=input('到达站：')
to_station=hanzi_to_pin(to_station)
print(date,from_station,to_station)

#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
ls2=data['data']['map']
print(ls2)
data=data['data']['result']
l=len(data)

p=' '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
m=input('想乘坐的列车类型：')
title='车次{}出发站{}到达站{}出发{}到达{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p) 
title=title.split(p)
for i in title:
    print(i.center(8),end='')
print()

for x in range(l):
    ls1=data[x].split('|')
    if ls1[3].startswith('{}'.format(m)):
        ls=[ls1[3],ls1[6],ls1[7],ls1[8],ls1[9],ls1[10],ls1[32],ls1[31],ls1[30],ls1[21],ls1[23],'--',ls1[28],'--',ls1[29],ls1[26],'--',ls1[1]]
        a=ls1[6]
        b=ls1[7]
        ls1[6]=ls2.get('{}'.format(a))
        ls1[7]=ls2.get('{}'.format(b))
        ls=[ls1[3],ls1[6],ls1[7],ls1[8],ls1[9],ls1[10],ls1[32],ls1[31],ls1[30],ls1[21],ls1[23],'--',ls1[28],'--',ls1[29],ls1[26],'--',ls1[1]]        
        for i in ls:
            print(str(i).center(10),end='')
        print('\n')
        


for x in range(l):
    ls1=data[x].split('|')
    if ls1[3].startswith('{}'.format(m)):
        ls=[ls1[3],ls1[6],ls1[7],ls1[8],ls1[9],ls1[10],ls1[32],ls1[31],ls1[30],ls1[21],ls1[23],'--',ls1[28],'--',ls1[29],ls1[26],'--',ls1[1]]
        a=ls1[6]
        b=ls1[7]
        ls1[6]=ls2.get('{}'.format(a))
        ls1[7]=ls2.get('{}'.format(b))
        ls=[ls1[3],ls1[6],ls1[7],ls1[8],ls1[9],ls1[10],ls1[32],ls1[31],ls1[30],ls1[21],ls1[23],'--',ls1[28],'--',ls1[29],ls1[26],'--',ls1[1]]
        ls3=sorted(ls,key=lambda data:ls[6]) 
        for i in ls3:
            print(str(i).center(10),end='')
        print('\n')

[].sorted(ls,key=lambda data:data[3]) 


























