#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年8月8日

@author: chen
'''
import requests
import json
import re
import time
import random
import string

class oder():
    def oder_tiojiao(self,token):
        u'''指定品类获取商品(POST请求)'''
        url = "http://store.51dinghuo.cc/api/bill/v8/order/new"
        #生成随机字符串
        ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 12))
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        data={"bills":[{"goodsList":[{"cartItemId":1,"amount":1,"activityId":0,"goodsId":1111111154,"price":30}],
        "main":{"receiveAddress":"上班吧","province":"广东","receiveId":2915,"receiveContactor":"陈","receiveContactInfo":"18612260669",
        "remark":"","county":"禅城区","city":"佛山","district":"A镇","mobileBillId":"E082CFA2-C604-4B31-A9C4-"+ran_str,"storeName":"佛山",
        "useBalance":0,"vendorId":2,"couponMoney":0},"billType":"bill_normal"}]}
        r = requests.post(url = url,json=data,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
        if ('成功' in fanhui)and code==200:
            #print ('提交商品生成订单_断言成功')
            return True
        else:
            print ('提交商品生成订单_断言失败')
            print (r.text)  
            return False

oder_up=oder()   