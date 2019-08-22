#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   07_wait.py
@Time    :   2019/8/21 14:01
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

base_url = 'http://www.baidu.com/'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get(base_url)


# 1.显示等待
# WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
#       driver ：浏览器驱动。
#       timeout ：最长超时时间，默认以秒为单位。
#       poll_frequency ：检测的间隔（步长）时间，默认为0.5S。
#       ignored_exceptions ：超时后的异常信息，默认情况下抛NoSuchElementException异常
#       until(method, message=‘’)-----调用该方法提供的驱动程序作为一个参数，直到返回值为True。
#       until_not(method, message=‘’)---调用该方法提供的驱动程序作为一个参数，直到返回值为False。
# presence_of_element_located()方法判断元素是否存在。
element = WebDriverWait(driver, 5, 0.5).until(
    EC.presence_of_element_located((By.ID, 'kw'))
    )
element.send_keys('要搜索的内容')
time.sleep(3)

driver.quit()


# 2. 隐式等待

