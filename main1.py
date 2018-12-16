#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年12月6日

@author:主函数用于控制全局
'''
import s_denglu
import s_shouye,s_oder_tijiao,s_Cat_add
from s_all_pinlei import *
import s_sousuo_shangpin,s_zhiding_pinlei,s_Cat_list
import s_oder_list,s_coupon_list
if __name__ == "__main__":
    fan1=s_denglu.kai.post_denglu()#登录
#     s_shouye.diao.shouye(fan1)#获取首页
#     s_sousuo_shangpin.Detian.get_phone(fan1)#搜索商品
#     fan3=allpinglei.all_pinlei(fan1) #获取全部分类
#     s_zhiding_pinlei.pinglei.zh_pinlei(fan1)#指定品类
    s_Cat_list.list_Cat.Cat_list(fan1)
    s_oder_list.list_1.list_oder(fan1)
    s_coupon_list.coupon.list_coupon(fan1)
    #add_cat=s_Cat_add.Cat_add.Cat_add(fan1)
#    oder=s_oder_tijiao.oder_up.oder_tiojiao(fan1)

    

    
    
    