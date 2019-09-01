#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_keyword.py
@Time    :   2019/8/30 23:59
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from selenium import webdriver
from basic.find_element import FindElement
from time import sleep


class RegisterKeyword(object):
    def __init__(self):
        pass

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome('../tools/chromedriver.exe')
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入测试地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def get_element(self, key):
        self.fe = FindElement(self.driver)
        return self.fe.get_element(key)

    # 输入元素
    def send_element_key(self, key, value):
        get_element = self.get_element(key)
        get_element.send_keys(value)

    # 点击元素
    def click_element(self, key):
        self.fe.get_element(key).click()

    # 页面等待
    @staticmethod
    def wait_loading():
        sleep(3)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome('../tools/chromedriver.exe')
    driver.get(register_url)
    rk = RegisterKeyword()
    print(rk.get_element('register_email'))
    driver.close()
