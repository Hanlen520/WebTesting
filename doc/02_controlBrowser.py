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


base_url = 'http://www.5itest.cn/register'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)


# browser.set_window_size(400, 800)
browser.maximize_window()
browser.quit()
