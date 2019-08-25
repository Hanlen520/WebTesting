#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register.py
@Time    :   2019/8/25 9:42
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# 1.启动要测试页面
# 全局定义注册页面地址
register_url = 'http://www.5itest.cn/register'
# 创建 driver 对象
driver = webdriver.Chrome('../tools/chromedriver.exe')
# 打开测试页面
driver.get(register_url)
# 等待页面加载
sleep(3)
# 通过title是否加载成功，来判断注册页面是否加载成功了，下面的打印结果说明了该对象存在于内存对象中也就是title加载成功了
print(EC.title_contains('注册'))


# 关闭浏览器(close关闭单个页面)
driver.close()
