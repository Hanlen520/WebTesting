#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   ddt_introduction.py
@Time    :   2019/8/30 10:35
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import unittest
import ddt

@ddt.ddt
class DDTExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print(cls.__name__)

    @classmethod
    def tearDownClass(cls) -> None:
        print('...end...')

    @ddt.data(
        [1, 2],
        [3, 4],
        [5, 6]
    )
    @ddt.unpack
    def test_add(self, a, b):
        print(a + b)


if __name__ == "__main__":
    unittest.main()

