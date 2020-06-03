# -*- coding:utf-8 -*-
# @Time :2020/2/12 15:10
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :test_suite.py

import unittest
import os
import HTMLTestRunnerNew as HTMLTestRunner
from page_testcase.testcase import page_case

# 创建测试套件
suite = unittest.TestSuite()

# 创建测试报告相关参数
report_name = 'shopxo测试报告'
report_title = '添加购物车测试报告'
report_desc = '登录添加购物车并查看是否成功'
report_path = './report/'
report_file = './report/report1.html'

# 判断report_path是否存在，如果不存在则新增一个该路径
if not os.path.exists(report_path):
    os.mkdir(report_path)
else:
    pass

# 生成测试报告
with open(report_file, 'wb') as report:
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(page_case))
    htmlrunner = HTMLTestRunner.HTMLTestRunner(stream=report, title=report_title, tester='枫', description=report_desc,
                                               verbosity=2)
    htmlrunner.run(suite)
report.close()
