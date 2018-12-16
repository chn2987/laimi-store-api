#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017年9月28日
@author: unittest自动化框架(可以调用)
'''
import unittest
import os
import HTMLTestRunner
import time
now = time.strftime("%Y-%m-%d %H-%M-%S")#获取当前时间及日期
# 用例路径
case_path = os.path.join(os.getcwd(),"//chenwei//python//zskx/laimi//laimi-store1")
# 报告存放路径
report_path = os.path.join(os.getcwd(), "//chenwei//python//zskx/laimi//laimi-store1//html_baogao")
def all_case():
    discover = unittest.defaultTestLoader.discover(case_path,
                                                    pattern="main.py",
                                                    top_level_dir=None)
    print(discover)
    return discover

if __name__ == "__main__":
    # runner = unittest.TextTestRunner()
    # runner.run(all_case())

    # html报告文件路径
    #report_abspath = os.path.join(report_path, now+"result.html")#加now就每次生成一个报告，不加则覆盖
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'unittest自动化测试报告,测试结果:',
                                           description=u'用例执行情况:')

    # 调用add_case函数返回值
    runner.run(all_case())
    fp.close()
