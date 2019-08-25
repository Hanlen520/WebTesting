#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   06_asseert.py
@Time    :   2019/8/20 23:23
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
import time


base_url = 'https://www.baidu.com/'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get(base_url)

time.sleep(1)

print("直接访问链接后页面元素获取")
title = driver.title
print('first title: %s' % title)
current_url = driver.current_url
print('first current_url: %s' % current_url)


driver.find_element_by_id('kw').send_keys('python')
driver.find_element_by_id('su').click()
time.sleep(1)
print('搜索关键词后页面元素获取')
title2 = driver.title
print('second title: %s' % title2)
current_url2 = driver.current_url
print('first current_url2: %s ' % current_url2)
kw_text = driver.find_element_by_id('kw').text
print('nums text: %s' % kw_text)


driver.quit()
