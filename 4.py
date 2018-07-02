# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 16:29:51 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
for i in range(0,4972,44):
    url='https://s.taobao.com/search?q=%E8%A3%A4%E5%AD%90&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(i)
    data=r.urlopen(url).read().decode('utf-8')
    import json
    data=json.loads(data)
    l=len(data)
    for x in range(l):
        a=data['mods']['itemlist']['data']['auctions'][x]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][x]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][x]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][x]['nick']
        e=data['mods']['itemlist']['data']['auctions'][x]['item_loc']
        print('商品名为：{}，价格为：{}，付款人数为：{}，店铺名为：{}，地址为：{}'.format(a,b,c,d,e))
f=open('./c.csv','a')#csv表格文件，以逗号分割
for i in range(1000):
    f.write("{},{}\n".format(i,'我'))
f.close()