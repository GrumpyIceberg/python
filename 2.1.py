# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 18:12:10 2018

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
def msg(x):
    a=data['list'][x]['main']['temp']
    b=data['list'][x]['main']['temp_max']
    c=data['list'][x]['main']['temp_min']
    d=data['list'][x]['main']['pressure']
    e=data['list'][x]['weather'][0]['main']
    g=data['city']['name']
    f=data['list'][x]['dt_txt']
    print('{}'.format(f),int(b)*'*','{}{}的天气情况是{}，温度为{}，最高温度{}，最低温度{}，气压为{}'.format(g,f,e,a,b,c,d))
msg(0)
msg(2)
msg(4)
msg(8)
msg(10)
msg(12)
msg(16)
msg(18)


