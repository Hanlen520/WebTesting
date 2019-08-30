#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_ddt_cases.py
@Time    :   2019/8/30 14:19
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import ddt
from page_object_model.register_business import RegisterBusiness
from selenium import webdriver
import unittest
from time import sleep


@ddt.ddt
class RegisterDdtCases(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_url = 'http://www.5itest.cn/register'
        cls.driver = webdriver.Chrome('../tools/chromedriver.exe')
        cls.driver.maximize_window()
        cls.driver.get(cls.register_url)
        sleep(3)
        cls.rb = RegisterBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        sleep(2)
        cls.driver.close()

    # 邮箱错误测试的测试用例
    @ddt.data(
        # 顺序分别是：注册邮箱、用户昵称、注册密码、验证码、错误信息定位元素、错误提示信息
        ['123', 'test01', 'test01abc', 'tyu9'],
        ['@163.com', 'test01', 'test01abc', 'tyu9'],
        ['@163', 'test01', 'test01abc', 'tyu9']
    )
    @ddt.unpack
    def test_ddt_email_error(self, register_email, nickname, password, captcha):
        register_email_error = self.rb.register_email_error(register_email, nickname, password, captcha)
        print("register_email_error: ", register_email_error)
        self.assertFalse(register_email_error, '你输入的邮箱错误，但此条测试用例执行成功')


if __name__ == "__main__":
    unittest.main()
