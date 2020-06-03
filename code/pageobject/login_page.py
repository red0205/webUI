# -*- coding:utf-8 -*-
# @Time :2020/2/17 17:17
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :login_page.py

from class_23.pagebase.page_base import pagebase


class login(pagebase):

    login_url = 'http://39.98.138.157/shopxo/index.php?s=/index/user/logininfo.html'

    def sign_in(self, name, keyword):
        self.wait('//label[text()="登录账号"]', '进入登录页面')
        self.input('//input[@name="accounts"]', name)
        self.input('//input[@name="pwd"]', keyword)
        self.click('//button[text()="登录"]')
        self.wait('//em[text()="feng2，欢迎来到"]', '登录')


if __name__ == '__main__':
    name = 'feng2'
    keyword = 'zhx159753'
    Login = login('cc', login.login_url)
    Login.sign_in(name, keyword)
    Login.quit()
