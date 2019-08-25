#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   13_callJavaScript.py
@Time    :   2019/8/24 12:46
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from time import sleep


base_url = 'https://www.baidu.com'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)

# window.scrollTo()方法用于设置浏览器窗口滚动条的水平和垂直位置。方法的第一个参数表示水平的左间距，第二个参数表示垂直的上边距。
browser.set_window_size(500, 500)
browser.find_element_by_id('kw').send_keys('百度')
browser.find_element_by_id('su').click()
sleep(2)

# 通过javascript设置浏览器窗口的滚动条位置
js = "window.scrollTo(100, 450);"
browser.execute_script(js)
sleep(2)

browser.quit()
