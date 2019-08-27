#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   find_element.py
@Time    :   2019/8/27 14:45
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   将页面查找元素的功能封装
"""

from util.read_ini import ReadIni


class FindElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, key):
        ri = ReadIni()
        data = ri.get_value(key=key)
        by = data.split('>')[0]
        value = data.split('>')[1]
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_className(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            file_path = '../image/no_element.png'
            self.driver.save_screenshot(file_path)


if __name__ == "__main__":
    fe = FindElement()
    fe.get_element('register_nickname')