#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   08_switchWindow.py
@Time    :   2019/8/22 21:48
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
import time

base_url = 'https://www.baidu.com/'


browser = webdriver.Chrome('../tools/chromedriver.exe')
# 隐式等待10秒
browser.implicitly_wait(10)
browser.get(base_url)


# 获得搜索窗口的句柄
search_windows = browser.current_window_handle
browser.find_element_by_link_text('登录').click()
browser.find_element_by_link_text('立即注册').click()

# 活得当前打开窗口的句柄
all_handles = browser.window_handles

# 进入注册窗口
for handle in all_handles:
    if handle != search_windows:
        browser.switch_to.window(handle)
        print('now register window!')
        browser.find_element_by_name('account').send_keys('username')
        browser.find_element_by_name('password').send_keys('password')
        time.sleep(2)

browser.quit()
