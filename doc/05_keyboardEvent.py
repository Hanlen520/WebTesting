#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   05_keyboardEvent.py
@Time    :   2019/8/20 22:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


base_url = 'https://www.baidu.com/'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get(base_url)


# 先输入百度
driver.find_element_by_id('kw').send_keys('百度')
# 1.删除度
driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
time.sleep(3)

# 2.键入空格
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys('加入空格')
time.sleep(5)

# 3.ctrl+a 全选输入框里的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
time.sleep(3)

# 4.ctrl+x 剪切输入框里的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# 5. ctrl+v 粘贴剪切的内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
time.sleep(3)

# 6. 回车
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(3)


driver.quit()
