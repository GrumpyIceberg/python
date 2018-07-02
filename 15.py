# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:59:05 2018

@author: Administrator
"""

"""
Created on Fri Jun 29 09:45:11 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""
class weather:
    def __init__(self,data,temp,description,pressure):
        self.data=data
        self.temp=temp
        self.description=description
        self.pressure=pressure
    def msg(self):
        print('现在时间为：{}\n温度是：{}\n天气情况是：{}\n气压是：{}'.format(self.data,self.temp,self.description,self.pressure))
a=weather(11,35,'晴',22.6)
b=weather(12,35,'晴',22.7)
c=weather(13,37,'晴',22.8)
a.msg()
b.msg()
c.msg()
