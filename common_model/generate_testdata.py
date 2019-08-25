#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   generate_testdata.py
@Time    :   2019/8/25 21:38
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import random

# 1. 生成测试邮箱数据
for i in range(5):
    register_test_email = ''.join(random.sample('abcdefgh1234567890', 8)) + '@163.com'
    print("生成的五组测试邮箱账号为：", register_test_email)


# 2. 同理，生成测试昵称数据
for i in range(5):
    register_nickname = ''.join(random.sample('abcdefghijk', 5))
    print("生成的五组测试用户昵称为：", register_nickname)
