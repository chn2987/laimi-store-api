#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月21日

@author:实现商品搜索(POST请求)
'''
#__________________________________使用面向对象方式接口(搜索商品)____________________________________________________________

import requests   #先导入包,这是必须的
import json
import re
class AddBook(object):
    def __init__(self, name,phone='chen'):
        self.name = name
        self.phone=phone
    def get_phone(self,token):
        u'''获取叮趣首页接口(POST请求)'''
        if self.phone:
            url = 'http://store.51dinghuo.cc/api/goods/v3/area/search'
            data={
            "limit": 20,
            "offset": 0,
            "onlyCode": "false",
            "keyword": "chen"
            }
            headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
            r = requests.post(url,json = data,headers = headers)
            #chen=r.json()#把响应的json数据写入到chen
    #             print(r.url)#返回url地址
    #             print (r.status_code)#响应状态码  
            #print(r.text)#打印响应数据
            a=r.text
            chen='小当家原味啤酒' in a #判断a中是否包含'小当家'，若包含则为true
            
            if chen==True:
                #print("搜索商品_断言成功")
                return True
            else:
                print("搜索商品_断言失败")
                return False
        else:
            print('没有搜索的条件')

Detian = AddBook(5)




