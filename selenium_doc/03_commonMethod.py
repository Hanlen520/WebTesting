#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   03_commonMethod.py
@Time    :   2019/8/20 12:12
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
import time

base_url = 'https://www.baidu.com'

browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)

# 1. 清除、输入、点击
browser.find_element_by_id('kw').clear()
browser.find_element_by_id('kw').send_keys('python')
browser.find_element_by_id('su').click()
time.sleep(2)


# 2.提交
search_text = browser.find_element_by_id('kw')
search_text.send_keys('selenium')
search_text.submit()
time.sleep(3)


# 3. 其他常用方法
size = browser.find_element_by_id('kw').size
print("返回元素的尺寸：%s" % size)

text = browser.find_element_by_id('cp').text
print("返回元素的文本：%s" % text)

attribute = browser.find_element_by_id('kw').get_attribute('type')
print("返回元素的属性：%s" % attribute)

result = browser.find_element_by_id('kw').is_displayed()
print("返回元素是否可见：%s" % result)


browser.quit()
