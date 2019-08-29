#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   discern_captcha.py
@Time    :   2019/8/29 23:22
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   图片验证码识别模块
"""

from api.ShowapiRequest import ShowapiRequest
from PIL import Image
from time import sleep
from selenium import webdriver


class DiscernCaptcha(object):
    def __init__(self, driver):
        self.driver = driver

    # 获取照片
    def get_captcha_code_image(self, file_name):
        self.driver.save_screenshot(file_name)
        captcha_image = self.driver.find_element_by_id('getcode_num')
        left = captcha_image.location['x']
        top = captcha_image.location['y']
        right = captcha_image.size['width'] + left
        height = captcha_image.size['height'] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        sleep(3)

    # 识别图片
    def discern_image(self, file_name):
        self.get_captcha_code_image(file_name)
        # 解析验证码图片中的文字（用第三方的图片验证码识别接口 ShowApiRequest）
        r = ShowapiRequest("http://route.showapi.com/184-4", "48120", "12c017278c0845c2bcda177212d2d2ac")
        r.addBodyPara("img_base64", "")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        text = res.json()["showapi_res_body"]["Result"]
        return text


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome('../tools/chromedriver.exe')
    driver.get(register_url)
    driver.maximize_window()
    dc = DiscernCaptcha(driver)
    file_name = '../image/discern_captcha/code_image.png'
    dc.get_captcha_code_image(file_name)
    dc.discern_image(file_name)
    driver.close()