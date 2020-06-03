# -*- coding:utf-8 -*-
# @Time :2020/2/17 22:07
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :index_page.py

from pagebase.page_base import pagebase
from selenium.webdriver.common.action_chains import ActionChains


class indexpage(pagebase):

    url = 'http://39.98.138.157/shopxo/index.php'

    def choose_all(self):
        e1 = self.get_xpath('//a[@title="食品饮料"]')
        ActionChains(self).move_to_element(e1).perform()
        self.wait('//span[text()="休闲零食"]', '点击休闲零食')
        self.click('//span[text()="休闲零食"]')