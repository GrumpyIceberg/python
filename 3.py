# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 08:49:36 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
def tao(x):
    a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][x]['nick']
    e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
    print('商品名为：{}，价格为：{}，付款人数为：{}，店铺名为：{}，地址为：{}'.format(a,b,c,d,e))
tao(1)
tao(2)
tao(3)


for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    d=data['mods']['itemlist']['data']['auctions'][i]['nick']
    e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
    print('商品名为：{}，价格为：{}，付款人数为：{}，店铺名为：{}，地址为：{}'.format(a,b,c,d,e))

lis=[]
for i in range(44):
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    c=float(b)
    lis.append(c)
sorted(lis)
lis1=sorted(lis,reverse=True)
print(lis1)

import re
lis=[]
for i in range(44):
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    m=re.sub("\D","",c)
    n=float(m)
    lis.append(n)
sorted(lis)
lis1=sorted(lis,reverse=True)
print(lis1)

for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    f=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if(f=='0.00'):
        print('商品名为：{}，价格为：{}'.format(a,b))

        
#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》icon 列表  
#-》index 0字典-》 iconPopupComplex 字典-》subIcons 列表-》index 0 字典-》icon_content变量
for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    try:
        g=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]['icon_content']
        print('商品名称为{}，提供{}'.format(a,g))
    except Exception as err:
        print('商品名称为{}，不提供15天退货'.format(a))

for i in range(44):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    f=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if(f=='0.00'):
        try:
            g=data['mods']['itemlist']['data']['auctions'][i]['icon'][0]['iconPopupComplex']['subIcons'][0]['icon_content']
            if(g=='15天退货'):
                print('商品名称为{}，包邮，提供{}'.format(a,g))            
        except Exception as err:
            continue

 
        

            
    
    
    
    
    
    
    
    