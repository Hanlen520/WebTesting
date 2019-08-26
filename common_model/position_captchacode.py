#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   position_captchacode.py
@Time    :   2019/8/26 12:28
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from PIL import Image
from selenium import webdriver
from time import sleep

register_url = 'http://www.5itest.cn/register'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get(register_url)
sleep(3)

# (1)将含有验证码的页面截图保存下来（这里指的是注册页面）
driver.save_screenshot('image/register_screenshot.png')

# (2)定位图片验证码图片的坐标
code_element = driver.find_element_by_id('getcode_num')
print("验证码的图片左上角顶点的坐标为：", code_element.location)
print("验证码的图片高宽的大小为：", code_element.size)

# (3)计算图片四个定点的位置
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
image = Image.open('image/register_screenshot.png')

# (4)将图片验证截取
code_image = image.crop((left, top, right, height))
code_image.save('image/captchcode_image.png')


driver.close()
