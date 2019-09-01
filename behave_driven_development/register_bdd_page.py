#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_bdd_page.py
@Time    :   2019/9/1 18:06
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""
from behave_driven_development.bdd_base import BDDPage
from selenium.webdriver.common.by import By


class RegisterPage(BDDPage):
    def __init__(self, context):
        super(RegisterPage, self).__init__(context.driver)

    def send_useremail(self, useremail):
        self.find_element(By.ID, "register_email").send_keys(useremail)

    def send_userename(self, username):
        self.find_element(By.ID, "register_nickname").send_keys(username)

    def send_password(self, password):
        self.find_element(By.ID, "register_password").send_keys(password)

    def send_code(self, captcha_code):
        self.find_element(By.ID, "captcha_code").send_keys(captcha_code)

    def click_register_button(self):
        self.find_element(By.ID, "register-btn").click()
