#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   09_alert.py
@Time    :   2019/8/22 22:30
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


base_url = 'https://www.baidu.com/'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.implicitly_wait(10)
driver.get(base_url)

# 鼠标悬停至 “设置” 链接
link = driver.find_element_by_link_text('设置')
ActionChains(driver).move_to_element(link).perform()

# 打开搜索设置
driver.find_element_by_link_text('搜索设置').click()
time.sleep(3)

# 点击 “搜索设置”
driver.find_element_by_class_name('prefpanelgo').click()
time.sleep(3)

# 接受警告框prefpanelgo
driver.switch_to.alert.accept()
time.sleep(3)

driver.quit()

