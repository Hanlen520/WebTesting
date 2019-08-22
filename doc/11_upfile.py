#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   11_upfile.py
@Time    :   2019/8/23 0:12
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
import os


driver = webdriver.Chrome('../tools/chromedriver.exe')
file_path = "file:///" + os.path.abspath('upfile.html')
driver.get(file_path)

# 定位上传按钮的位置
driver.find_element_by_name('file').send_keys(os.path.abspath('upfile.txt'))
driver.quit()
