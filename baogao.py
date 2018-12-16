#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2018年6月1日

@author: chen
'''
import requests
import json
import re
import time
class shangping():
    def sp_sousuo(self,token):
        u'''商店端登录接口(POST请求)'''
        # wo= open('G:\\eclipse_1\\普通学习\\叮趣接口学习\\123.txt', 'r')
    #     wo= open(r'G:\eclipse_1\web_selenium1\test\123.txt', 'r')
    #     shu1 = wo.readline()
    #     shu=shu1.strip('\n')
        url = "http://store.51dinghuo.cc/api/goods/v3/area/search"
        data = {"limit":20,"offset":0,"onlyCode":"false","keyword":"chen"}
        headers = {"Content-Type":"application/json","Laimi-Client-Version": "ios.store.client:2.28.0","Cookie":"SESSION="+(token)}
        #下面三行获取登陆cooke
        #session=requests.session()
        #set= session.post(url,json=data, headers=headers)#以session方式提交数据
        r = requests.post(url, json=data, headers=headers)
        chen = r.json() # 把响应的json数据写入到chen
        print (r.text)   #获取响应报文 
        #result = json.dumps(chen, encoding='UTF-8', ensure_ascii=False)#字典转中文显示
        #json_str = json.dumps(result)#把字典转成json格式
        '''
        newjson=json.dumps(chen,ensure_ascii=False)#把字典转成json格式,并以中文显示
        print(chen)
        chen1=json.dumps(cookies,ensure_ascii=False)
        rr=re.findall("SESSION\":(.+)}",chen1)#正则匹配json数据
        a= eval("" .join(rr))#把字段转成str并去掉双引号
        print(a)
        print(cookies)
        time.sleep(1.5) 
       #判断json文件是否有指定字符串(目前不会使用字典判断)
        if ('三水区' in newjson) :
            print ('元素包含成功_登录成功')
            return a
        else:
            print ('没有匹配到相关元素_登录异常')
     '''       
sp=shangping()
#kai.post_denglu()

