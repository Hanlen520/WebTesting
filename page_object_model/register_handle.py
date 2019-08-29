#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_handle.py
@Time    :   2019/8/29 15:07
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   给register_page中找到的元素赋值
"""

from page_object_model.regitser_page import RegisterPage
from selenium import webdriver
from time import sleep

class RegisterHandle(object):
    def __init__(self, driver):
        self.rp = RegisterPage(driver)

    # 输入注册邮箱
    def send_register_email(self, email):
        self.rp.get_register_email().send_keys(email)

    # 输入用户昵称
    def send_register_nickname(self, nickname):
        self.rp.get_register_nickname().send_keys(nickname)

    # 输入注册密码
    def send_register_password(self, password):
        self.rp.get_register_password().send_keys(password)

    # 输入验证码
    def send_register_captcha(self, captcha):
        self.rp.get_getcode_num().send_keys(captcha)

    # 获取错误信息
    def get_user_text(self, error_info, *kwargs):
        text = None
        if error_info == "register_email_error":
            text = self.rp.get_register_email_error()
        elif error_info == 'register_nickname_error':
            text = self.rp.get_register_nickname_error()
        elif error_info == 'register_password_error':
            text = self.rp.get_register_password_error()
        elif error_info == 'captcha_code_error':
            text = self.rp.get_captcha_code_error()
        else:
            print("error element not found")
        return text

    # 点击注册按钮
    def click_register_btn(self):
        self.rp.get_register_btn().send_keys()

    # 获取注册按钮的文字，如果有的话就说明注册不成功还停留在注册页面，如果不存在的话说明已经跳转到新的页面也就是注册成功了
    def get_register_btn_text(self):
        return self.rp.get_register_btn().text()


if __name__ == "__main__":
    register_url = 'http://www.5itest.cn/register'
    driver = webdriver.Chrome('../tools/chromedriver.exe')
    driver.get(register_url)
    rh = RegisterHandle(driver)
    rh.send_register_email('jjij@163.com')
    rh.send_register_nickname('MiFan')
    rh.send_register_password('123@123abc')
    rh.send_register_captcha('qwer')
    rh.click_register_btn()
    print(rh.get_register_btn_text)
    sleep(5)
    driver.close()
