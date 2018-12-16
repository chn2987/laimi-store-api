#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年8月10日

@author: chen
'''
import requests
import json
import re
import time
class Cat_1():
    def Cat_add(self,token):
        u'''指定品类获取商品(POST请求)'''
        url = "http://store.51dinghuo.cc/api/cart/v1/add"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        data={
        "insert": [{
        "amount": 1,
        "activityId": 0,
        "goodsId": 1111111154,
        "price": 30,
        "activityType": 0
        }]
        }
        r = requests.post(url = url,json=data,headers = headers)
        print (r.text)   #获取响应报文
        code=r.status_code
#         fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
#         if ('旧环境01扎啤原味啤酒2000ml*2(整件)' in fanhui)and code==200:
#             #print ('指定分类筛选商品_断言成功')
#             return True
#         else:
#             print ('指定分类筛选商品_断言失败')
#             return False
Cat_add=Cat_1()    