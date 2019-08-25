#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   12_cookie.py
@Time    :   2019/8/23 10:11
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from selenium import webdriver
from time import sleep


base_url = 'https://www.baidu.com/'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)

# 1. 获取 cookie 信息
cookies = browser.get_cookies()
print(cookies)
sleep(2)
browser.quit()

# 2. cookie 写入
browser.add_cookie(
    {
        'name': 'add-cookie',
        'value': 'add-cookie-value'
    }
)
# 遍历cookies打印cookie信息
for cookie in browser.get_cookies():
    print("%s ---> %s" % (cookie['name'], cookie['value']))
sleep(2)
browser.quit()
