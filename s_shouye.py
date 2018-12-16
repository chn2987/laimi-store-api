#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年05月29日

@author:首页获取(GET请求)
'''
import requests
import json
import re
import time
import s_denglu
class log_sy:
    def shouye(self,token):
        u'''获取首页接口(GET请求)'''
        url = "http://store.51dinghuo.cc/api/promotion/v3/home/list"
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        r = requests.get(url = url,headers = headers)
        #print (r.text)   #获取响应报文
        code=r.status_code
        fanhui=json.dumps(r.text,ensure_ascii=False)#把字典转成json格式,并以中文显示
        if ('掌上快销佛山' in fanhui) and code==200:
            #print ('获取首页指定元素成功')
            return '掌上快销佛山'
        else:
            print ('首页元素获取失败')
            return 'false' 

diao=log_sy()    
#cooke=denglu.kai.post_denglu()
time.sleep(1) 