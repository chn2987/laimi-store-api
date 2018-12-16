#i/usr/bin/env python
#coding=utf-8
'''
Created on 2018年05月29日
@author:商店端登录接口(POST请求)
'''
import requests
import json
import re
import time
class logout:
    def post_denglu(self):
        u'''商店端登录接口(POST请求)'''
        # wo= open('G:\\eclipse_1\\普通学习\\叮趣接口学习\\123.txt', 'r')
    #     wo= open(r'G:\eclipse_1\web_selenium1\test\123.txt', 'r')
    #     shu1 = wo.readline()
    #     shu=shu1.strip('\n')
        url = "http://store.51dinghuo.cc/api/auth/token"
        data = {"uuId":"2BFBB28A-5D0D-48E9-B0B3-2185E827DC3E", "isWeb":"true", "loginName":"18612260669", "loginPass":"123456"}
        headers = {'Content-Type':'application/json'}  # 引用变量self.phone(拼接字符串)
        #下面三行获取登陆cooke
        session=requests.session()
        set= session.post(url,json=data, headers=headers)#以session方式提交数据
        cookies=requests.utils.dict_from_cookiejar(session.cookies)#将获取的cooke转成字典
        #r = requests.post(url, json=data, headers=headers)
        chen = set.json() # 把响应的json数据写入到chen
        #print (r.text)   #获取响应报文 
        #result = json.dumps(chen, encoding='UTF-8', ensure_ascii=False)#字典转中文显示
        #json_str = json.dumps(result)#把字典转成json格式
        newjson=json.dumps(chen,ensure_ascii=False)#把字典转成json格式,并以中文显示
        #print(chen)
        chen1=json.dumps(cookies,ensure_ascii=False)
        rr=re.findall("SESSION\":(.+)}",chen1)#正则匹配json数据
        a= eval("" .join(rr))#把字段转成str并去掉双引号
        #print(a)
        print(cookies)
        time.sleep(1.5) 
       #判断json文件是否有指定字符串(目前不会使用字典判断)
        if (u'禅城区' in newjson) :
            print ('denglu__ture')
            return a
        else:
            print ('denglu__fales')
            
kai=logout()
#kai.post_denglu()

