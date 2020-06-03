# -*- coding:utf-8 -*-
# @Time :2020/2/17 22:07
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :index_page.py

from class_23.pageobject.login_page import login
from selenium.webdriver.common.action_chains import ActionChains


class indexpage(login):

    url = 'http://39.98.138.157/shopxo/index.php'

    def choose_all(self):
        e1 = self.driver.find_element_by_xpath('//a[@title="食品饮料"]')
        ActionChains(self.driver).move_to_element(e1).perform()
        self.wait('//span[text()="休闲零食"]', '点击休闲零食')
        self.click('//span[text()="休闲零食"]')

    def choose(self):
        self.click('//a[text()="登录"]')
        self.wait('//label[text()="登录账号"]', '进入登录页面')


if __name__ == '__main__':
    name = 'feng2'
    keyword = 'zhx159753'
    Index = indexpage('cc', indexpage.url)
    Index.choose()
    Index.sign_in(name, keyword)
    Index.choose_all()
