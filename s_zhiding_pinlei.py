#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年8月7日

@author: chen
'''
import requests
import json
import re
import time
class zhiding_pinglei():
    def zh_pinlei(self,token):
        u'''指定品类获取商品(POST请求)'''
        url = "http://store.51dinghuo.cc/api/v3/categoods"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        data={
        "categoryId": 143,
        "limit": 20,
        "offset": 0
        }
        r = requests.post(url = url,json=data,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
        if ('旧环境01扎啤原味啤酒2000ml*2(整件)' in fanhui)and code==200:
            #print ('指定分类筛选商品_断言成功')
            return True
        else:
            print ('指定分类筛选商品_断言失败')
            return False

pinglei=zhiding_pinglei()    
