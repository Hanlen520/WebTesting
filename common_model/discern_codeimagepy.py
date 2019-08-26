#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   discern_codeimagepy
@Time    :   2019/8/26 18:17
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   ShowapiRequest库从https://www.showapi.com/api/lookPoint/184下载
"""

from selenium import webdriver
from time import sleep
from api import ShowapiRequest

register_url = 'http://www.5itest.cn/register'
driver = webdriver.Chrome('../tools/chromedriver.exe')
driver.get(register_url)
sleep(5)
captcha_code = driver.find_element_by_xpath('//*[@id="captcha_code"]')
print('验证码的提示语：', captcha_code.get_attribute('placeholder'))
sleep(5)

# 解析验证码图片中的文字（用第三方的图片验证码识别接口 ShowApiRequest）
# 这里my_appId需要替换成你自己的my_appId，my_appSecret需要替换成你自己的my_appSecret
r = ShowapiRequest("http://route.showapi.com/184-4", "my_appId", "my_appSecret")
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"image/captchcode_image.png")  # 文件上传时设置
res = r.post()
text = res.json()["showapi_res_body"]["Result"]
captcha_code.send_keys(text)
sleep(3)

driver.close()
