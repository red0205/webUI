# -*- coding:utf-8 -*-
# @Time :2020/2/17 17:17
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :login_page.py

from pageobject.index_page import indexpage


class login(indexpage):
    login_url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    # 登录
    def sign_in(self, name, keys):
        self.click('//div[@class="menu-hd"]/a[1]')
        self.wait('//label[text()="登录账号"]', '进入登录页面')
        self.input('//input[@name="accounts"]', name)
        self.input('//input[@name="pwd"]', keys)
        self.click('//button[text()="登录"]')
        self.wait('//em[text()="feng2，欢迎来到"]', '登录')
