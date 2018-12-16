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
import ast
class Cat():
    def Cat_list(self,token):
        u'''查询用户购物车内是否有商品(GET请求)'''
        url = "http://store.51dinghuo.cc/api/cart/v1/list"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        r = requests.get(url = url,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
        if ('totalNumber' in fanhui)and code==200:
            wei=ast.literal_eval(r.text)#把字符串转成字典
            sp=wei['data']['cartInfo']['totalNumber']
            print ('购物车内有商品_%d条'%(sp))          
            return True
        else:
            print ('购物车暂无商品')
            print (r.text)
            return False

list_Cat=Cat()    
