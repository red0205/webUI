# -*- coding:utf-8 -*-
# @Time :2020/2/17 17:18
# @Author :student_枫
# @Email  :619251557@qq.com
# @File :seacher_page.py

from class_23.pagebase.page_base import pagebase


class seacher_page(pagebase):
    url = 'http://39.98.138.157/shopxo/index.php'

    # 搜索
    def search(self, str1):
        self.input('//input[@id="search-input"]', str1)
        self.click('//input[@id="ai-topsearch"]')


if __name__ == '__main__':
    Seacher = seacher_page('cc', seacher_page.url)
    Seacher.search('手机')
