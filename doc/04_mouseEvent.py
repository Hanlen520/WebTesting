#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   04_mouseEvent.py
@Time    :   2019/8/20 16:59
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


base_url = 'http://www.baidu.com/'
browser = webdriver.Chrome('../tools/chromedriver.exe')
browser.get(base_url)

# 定位到悬停元素处
above = browser.find_element_by_link_text('设置')
# 对元素执行鼠标悬停操作
ActionChains(browser).move_to_element(above).perform()
time.sleep(5)

# 右击
ActionChains(browser).context_click().perform()
time.sleep(5)

# 定位到要双击的元素处
# double_click_element = browser.find_element_by_link_text('新闻')
# print(double_click_element)
# ActionChains(browser).move_to_element(double_click_element).double_click().perform()
# time.sleep(5)

# 拖动元素
drag_and_drop_element = browser.find_element_by_link_text('地图')
ActionChains(browser).move_to_element(drag_and_drop_element).drag_and_drop().perform()
time.sleep(5)

browser.quit()
