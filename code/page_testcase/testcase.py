# -*- coding:utf-8 -*-
# @Time :2020/2/17 21:20
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :testcase.py

from ddt import ddt, file_data
from class_23.pageobject.index_page import indexpage
import unittest


@ddt
class page_case(unittest.TestCase):

    def setUp(self) -> None:
        self.Index = indexpage('cc', indexpage.url)
        pass

    def tearDown(self) -> None:
        pass

    @file_data('para.yaml')
    def test_case1(self, **info):
        self.Index.choose()
        self.Index.sign_in(info.get('name'), info.get('keyword'))
        self.Index.choose_all()


if __name__ == '__main__':
    unittest.main()
