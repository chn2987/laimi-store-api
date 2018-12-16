#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年8月16日

@author: chen
'''
import requests
import json
import time
class oder_list():
    def list_oder(self,token):
        u'''获取订单列表(GET请求)'''
        url = "http://store.51dinghuo.cc/api/bill/v4/main/list/all?allCount=true&limit=20&offset=0"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        r = requests.get(url = url,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=r.text
        if ('掌上快销佛山' in fanhui)and('zskx_fs' in fanhui) and code==200:
            print ('我的订单列表获取_断言成功')
            #print(r.text)
            return True
        else:
            print ('我的订单列表获取_断言失败')
            return False
list_1=oder_list()
    