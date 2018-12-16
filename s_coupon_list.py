#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年8月16日

@author: chen
'''
import requests
import json
import time
from _ast import If
class coupon_list():
    def list_coupon(self,token):
        u'''获取订单列表(GET请求)'''
        url = "http://store.51dinghuo.cc/api/coupon/v3/list?allCount=true&limit=20&offset=0&status=0"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        r = requests.get(url = url,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=r.text
        
        if ('成功' in fanhui)and r.status_code==200:
            print(r.text)
            #print(r.status_code)#打印响应状态码
            if ('couponId' in fanhui) and r.status_code==200:
                #print ('优惠券列表获取成功_有未使用的优惠券')
                return True
            else:
                print('优惠券列表获取成功_但不存在有效优惠券')
            return True
        else:
            print ('获取我的优惠券列表_断言失败')
            return False
coupon=coupon_list()



