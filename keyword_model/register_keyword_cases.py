#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   register_keyword_cases.py
@Time    :   2019/9/1 0:03
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

from util.read_excel import ReadExcel
from keyword_model.register_keyword import RegisterKeyword


class RegisterKeywordCases(object):
    def __init__(self):
        self.rk = RegisterKeyword()
        self.excel_path = '../data/register_keyword_testdata.xls'

    # 执行关键字测试方法
    def run_keyword_method(self, keyword_method, operator_element='', send_value=''):
        print('keyword_method ---> ', keyword_method)
        print("operator_element ---> ", operator_element)
        print("send_value ---> ", send_value)
        execute_method = getattr(self.rk, keyword_method)
        print(execute_method)
        if operator_element is '' and send_value is not '':
            result = execute_method(send_value)
        elif operator_element is not '' and send_value is '':
            result = execute_method(operator_element)
        elif operator_element is '' and send_value is '':
            result = execute_method()
        else:
            result = execute_method(operator_element, send_value)
        return result

    # 执行关键词测试用例
    def run_keyword_excel_cases(self):
        handle_excel = ReadExcel(self.excel_path)

        # 获取 excel 关键词测试用例的条数
        cases_numbers = handle_excel.get_lines() - 1
        print("注册页获取到的关键词测试的测试用例条数为：%s" % cases_numbers)

        # 循环遍历测试用例
        if cases_numbers:
            # 第 0 行是标题行不作为用例执行
            for i in range(1, cases_numbers):
                # 获取测试用例的名称
                testcase_name = handle_excel.get_cell(i, 0)
                # 获取用例是否执行
                is_run = handle_excel.get_cell(i, 1)
                if is_run == 'yes':
                    keyword_method = handle_excel.get_cell(i, 2)
                    operator_element = handle_excel.get_cell(i, 3)
                    send_value = handle_excel.get_cell(i, 4)
                    except_result = handle_excel.get_cell(i, 5)
                    actual_result = handle_excel.get_cell(i, 6)

                    # 反射
                    self.run_keyword_method(keyword_method, operator_element, send_value)

                    # if except_result is not '':
                    #     except_value = self.run_keyword_method(keyword_method)
                else:
                    print('第 %s 条用例不执行，用例名称是: [%s]，无预期结果' % (i, testcase_name))
        else:
            print("略略略~，请检查你是否有写测试用例！")


if __name__ == "__main__":
    rkc = RegisterKeywordCases()
    # rkc.run_keyword_method('open_browser', '', 'chrome')
    # rkc.run_keyword_method('get_url', '', 'http://www.5itest.cn/register')
    rkc.run_keyword_excel_cases()
