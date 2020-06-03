# -*- coding:utf-8 -*-
# @Time :2020/2/17 17:18
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :page_base.py

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class pagebase(object):

    # 初始化
    def __init__(self, browser, url):
        self.open_browser(browser)
        self.driver.maximize_window()
        self.driver.get(url)
        self.driver.implicitly_wait(10)

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'ff':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'cc':
            self.driver = webdriver.Chrome()
        else:
            print('没有该浏览器，请重新输入。')

    # 打开网址
    def open_url(self, url):
        self.driver.get(url)

    # 关闭浏览器
    def quit(self):
        sleep(5)
        self.driver.quit()

    # 获取元素
    def get_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    # 点击操作
    def click(self, xpath):
        self.get_xpath(xpath).click()

    # 输入操作
    def input(self, xpath, keys):
        self.get_xpath(xpath).clear()
        self.get_xpath(xpath).send_keys(keys)

    # 等待断言
    def wait(self, xpath, step):
        WebDriverWait(self.driver, 10, 0.5).until(lambda e1: self.get_xpath(xpath), message=step+'失败')

    # 选择商品规格并加入购物车
    def choose(self, commodity, meal, color, size, num):
        self.switch()
        self.wait(commodity, '进入商品页面')
        self.t1 = self.get_xpath(commodity).text
        if meal != '无':
            self.click(meal)
        if color != '无':
            self.click(color)
        if size != '无':
            self.click(size)
            self.input('//input[@id="text_box"]', num)
            self.click('//button[@title="加入购物车"]')

    # 进入购物车查看商品
    def check(self, commodity):
        self.click('//span[text()="购物车"]')
        self.wait('//button[text()="结算"]', '进入购物车')
        self.t2 = self.get_xpath(commodity).text
        self.result(self.t1, self.t2)

    # 结果判断
    def result(self, t1, t2):
        if t1 == t2:
            print('商品加入购物车成功')
        else:
            print('商品加入购物车失败')

    # 切换页面
    def switch(self):
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 关闭页面
    def close(self):
        self.driver.close()