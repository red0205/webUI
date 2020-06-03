# -*- coding:utf-8 -*-
# @Time :2020/2/17 21:20
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :testcase.py

from ddt import ddt, file_data
from pageobject.seacher_page import seacher_page
import unittest


@ddt
class page_case(unittest.TestCase, seacher_page):

    def setUp(self) -> None:
        # 打开浏览器并进入网站
        self.project = seacher_page('cc', seacher_page.url)
        # 登录及校验登录
        self.project.sign_in('feng2', 'zhx159753')

    def tearDown(self) -> None:
        # 查看结果
        self.project.quit()

    @file_data('para.yaml')
    def testcase_01(self, **data):
        # 搜索商品
        self.project.search(data.get('search_goods'), data.get('goods_xpath'))

        # 选择商品规格并加入购物车
        self.project.choose(data.get('goods_choose'), data.get('goods_option1'), data.get('goods_option2'),
                            data.get('goods_option3'), data.get('goods_num'))

        # 进入购物车查看商品
        self.project.check(data.get('check'))
