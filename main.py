#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月30日
@author: 主函数、主要实现模块调用及断言处理(使用了装饰器 @classmethod)
'''
import unittest
import s_denglu
import s_shouye,s_sousuo_shangpin,s_all_pinlei
import s_zhiding_pinlei,s_Cat_list,s_oder_tijiao
import s_oder_list,s_coupon_list

#定义一个类并继承unittest模块TestCase
class BolgHome(unittest.TestCase):
    u'''商店端接口自动化'''
    fan1=s_denglu.kai.post_denglu()#返回值在全局
    @classmethod
    def setUpClass(self):#开始操作的函数
        pass
    @classmethod
    def tearDownClass(self):#结束函数
        pass  
    def test_01(self):#登录操作
        u'''判断是否登录成功：'''
        self.assertEqual(self.fan1, self.fan1, 'title不一致登录失败')
               
    def test_02(self):#搜索
        u'''通过条码或名称搜索商品'''
        self.find=s_sousuo_shangpin.Detian.get_phone(self.fan1)
        self.assertEqual(self.find, True, 'title不一致登录失败')
    def test_03(self):
        u'''获取首页信息'''
        self.sp=s_shouye.diao.shouye(self.fan1)
        self.assertEqual(self.sp, '掌上快销佛山', 'title不一致登录失败')
    def test_04(self):
        u'''全部分类查询'''
        self.all_fenlei=s_all_pinlei.allpinglei.all_pinlei(self.fan1)
        self.assertEqual(self.all_fenlei, True, 'title不一致登录失败')
        self.assertTrue(self.all_fenlei,'title不一致登录失败')#如果返回true则通过
    def test_05(self):
        u'''指定品类查看商品'''
        self.zhiding=s_zhiding_pinlei.pinglei.zh_pinlei(self.fan1)
        self.assertEqual(self.zhiding,True,'title不一致登录失败')
        
    def test_06(self):
        u'''判断购物车是否有商品'''
        self.Cat=s_Cat_list.list_Cat.Cat_list(self.fan1)
        self.assertEqual(self.Cat,True,'title不一致登录失败')
    def test_07(self):
        u'''提交生成订单'''
        self.oder=s_oder_tijiao.oder_up.oder_tiojiao(self.fan1)
        self.assertEqual(self.oder,True,'title不一致登录失败')
    def test_08(self):
        u'''查询我的订单列表'''
        self.oder_=s_oder_list.list_1.list_oder(self.fan1)
        self.assertEqual(self.oder_,True,'title不一致登录失败')
    def test_09(self):
        u'''获取我的优惠券列表'''
        self.coupon_list=s_coupon_list.coupon.list_coupon(self.fan1)
        self.assertEqual(self.coupon_list,True,'title不一致登录失败')
        
   
        
                 
if __name__ == "__main__":
    unittest.main()
