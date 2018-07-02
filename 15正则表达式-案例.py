# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 09:48:02 2018
爬取百度网页数据，用http:// 而不是其他
题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站
题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压

@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=92495750_hao_pg&wd=%E9%87%8D%E5%BA%86%E7%90%86%E5%B7%A5%E5%A4%A7%E5%AD%A6&oq=%25E8%25BF%2587%25E5%25B1%25B1%25E8%25BD%25A6%25E4%25B9%258B%25E6%2598%259F&rsv_pq=f61378cd0000c15f&rsv_t=6cf8EZ2Dr6VJgqgZIRqcmQ%2FPkXlL1CQR6hmKvNiXv5Z6KZKHJSsBzuj7IHPcECgqE%2FLOCDo7&rqlang=cn&rsv_enter=0&inputT=3736&rsv_sug3=25&rsv_sug1=24&rsv_sug7=100&bs=%E8%BF%87%E5%B1%B1%E8%BD%A6%E4%B9%8B%E6%98%9F'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls=re.compile('"title":"(.*?)"').findall(data)
ls1=re.compile('class="c-abstract">(.*?)</div><div',re.S).findall(data)
ls2=re.compile('style="text-decoration:none;">(.*?)&nbsp;</a>',re.S).findall(data)
for x in range(len(ls)):
    print('标题为：{}\n描述为：{}\n网站为:{}'.format(ls[x],ls1[x],ls2[x]).replace('<em>','').replace('</em>',''))
    


import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
date=r.urlopen(url).read().decode('utf-8')
print(date)
import re
tem=re.compile('"main":{"temp":(.*?),"',re.S).findall(date)
des=re.compile('"description":"(.*?)"').findall(date)
pre=re.compile('"pressure":(.*?),').findall(date)
for i in range(len(tem)):
    print('天气温度为：{}\n天气描述为：{}\n天气气压为:{}'.format(tem[i],des[i],pre[i]))

