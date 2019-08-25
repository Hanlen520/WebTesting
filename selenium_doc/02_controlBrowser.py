#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   02_controlBrowser.py
@Time    :   2019/8/19 22:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

# 1. 驱动浏览器控制窗口大小
from selenium import webdriver
import time


base_url = 'http://www.5itest.cn/register'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)


# browser.set_window_size(400, 800)
browser.maximize_window()
browser.quit()


# 2. 控制浏览器的前进、后退
browser_links = webdriver.Chrome('../tools/chromedriver.exe')
first_url = 'https://www.baidu.com/'
second_url = 'https://news.baidu.com/'

print("访问第一个链接：%s" % first_url)
browser_links.get(first_url)

time.sleep(1)
print("访问第二个链接：%s" % second_url)
browser_links.get(second_url)

time.sleep(1)
print("回退到第一个链接：%s" % first_url)
browser_links.back()

time.sleep(1)
print("前进到第二个链接：%s" % second_url)
browser_links.forward()

time.sleep(1)
browser_links.quit()


# 3. 页面刷新
refresh_url = 'http://www.baidu.com/'
browser_refresh = webdriver.Chrome('../tools/chromedriver.exe')
browser_refresh.get(refresh_url)
time.sleep(2)
browser_refresh.refresh()
browser_refresh.quit()

