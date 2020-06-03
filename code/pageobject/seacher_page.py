# -*- coding:utf-8 -*-
# @Time :2020/2/17 17:18
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :seacher_page.py

from pageobject.login_page import login


class seacher_page(login):
    seacher_url = 'http://39.98.138.157/shopxo/index.php'

    # 搜索
    def search(self, str1, commodity):
        self.input('//input[@id="search-input"]', str1)
        self.click('//input[@id="ai-topsearch"]')
        self.wait(commodity, '搜索')
        self.click(commodity)
