#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_testcases.py
@Time    :   2019/8/29 21:20
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from page_object_model.register_business import RegisterBusiness
from selenium import webdriver
import unittest


class RegisterTestcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_url = 'http://www.5itest.cn/register'
        cls.driver = webdriver.Chrome('../tools/chromedriver.exe')
        cls.driver.get(cls.register_url)
        cls.driver.maximize_window()
        cls.rb = RegisterBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

    # 注册邮箱错误，但用例执行成功
    def test_register_email_error(self):
        register_email_error = self.rb.register_email_error('23', 'test01', 'test01abc', 'abc4')
        if register_email_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")

    # 验证码错误，但用例执行成功‘
    def test_captcha_code_error(self):
        captcha_code_error = self.rb.captcha_code_error('test02@163.com', 'test02', 'test02abc', 'height')
        if captcha_code_error is True:
            print("账号注册失败，该用例执行成功")
        else:
            print("账号注册成功，该用例执行失败")


if __name__ == "__main__":
    unittest.main()
