#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register.py
@Time    :   2019/8/25 9:42
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   线性测试
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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


# 2.查找页面元素并传值给对应的元素处
# 邮箱地址
register_email = driver.find_element_by_id('register_email')
print("邮箱地址的提示语：", register_email.get_attribute('placeholder'))
register_email.send_keys('register_mail1@163.com')
# 用户名
register_nickname = driver.find_element_by_id('register_nickname')
print("用户名的提示语：", register_nickname.get_attribute('placeholder'))
register_nickname.send_keys('register_mail1')
# 密码
register_password = driver.find_element_by_id('register_password')
print("密码的提示语：", register_password.get_attribute('placeholder'))
register_password.send_keys('test@password')
# 验证码
captcha_code = driver.find_element_by_xpath('//*[@id="captcha_code"]')
print('验证码的提示语：', captcha_code.get_attribute('placeholder'))
captcha_code.send_keys('x7xx4')
# 检查《用户协议》是否加载出来了来判断
user_terms = driver.find_element_by_id('user_terms')
locator = (By.ID, 'user_terms')
print(WebDriverWait(driver, 1).until(EC.visibility_of_element_located(locator)))


# 关闭浏览器(close关闭单个页面)
driver.close()
