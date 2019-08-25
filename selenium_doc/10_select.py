#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   10_select.py
@Time    :   2019/8/22 22:49
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select
from time import sleep

base_url = 'https://www.baidu.com/'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.implicitly_wait(10)
driver.get(base_url)

# 鼠标悬停至“设置”链接
driver.find_element_by_name('设置').click()
sleep(2)
# 打开 “搜索设置”
driver.find_element_by_name('搜索设置').click()
sleep(2)
# 搜索结果显示条数
# Select类用于定位select标签。
sel = driver.find_element_by_xpath("//select[@id='nr']")
# select_by_value() 方法用于定位下接选项中的value值。
Select(sel).select_by_value('50')

driver.quit()

