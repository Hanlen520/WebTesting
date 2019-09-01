#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   bdd_base.py
@Time    :   2019/9/1 17:55
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium.webdriver.common.by import By


class BDDPage(object):
    def __init__(self, driver):
        self.driver = driver

    # 打开网页
    def get_url(self, url):
        self.driver.get(url)

    # 获取页面 title
    def get_page_title(self):
        return self.driver.title

    # 定位元素
    def find_element(self, *loc):
        self.driver.find_element(*loc)