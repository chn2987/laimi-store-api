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
class pinglei():
    def all_pinlei(self,token):
        u'''获取全部品类(GET请求)'''
        url = "http://store.51dinghuo.cc/api/v4/category"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        r = requests.get(url = url,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
        if ('小食品' in fanhui)and code==200:
            #print ('all分类查询_断言成功')
            #print(r.text)
            return True
        else:
            print ('all分类查询_断言失败')
            return False

allpinglei=pinglei()    




