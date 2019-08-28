#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@File    :   record_log.py
@Time    :   2019/8/28 19:15
@Author  :   Crisimple
@Github :    https://crisimple.github.io/
@Contact :   Crisimple@foxmail.com
@License :   (C)Copyright 2017-2019, Micro-Circle
@Desc    :   None
"""

import logging
import os
from datetime import datetime


class RecordLog(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)

        # 1. 在 console 中输出日志文件
        # 能够将日志信息输出到sys.stdout, sys.stderr 或者类文件对象
        # 日志信息会输出到指定的stream中，如果stream为空则默认输出到sys.stderr。
        console = logging.StreamHandler(stream=None)
        # 将sys.stderr中的信息添加到logger中
        self.logger.addHandler(console)
        # 输出调试信息
        self.logger.debug("这是一条在控制台线上的log")
        # 关闭流
        console.close()
        # 移除
        self.logger.removeHandler(console)

        # 2.将log信息输出到log文件中
        # 2.1 先定位看将log文件输出到哪里去
        current_dir = os.path.dirname(os.path.abspath(__file__))
        print(current_dir)  # D:\MySpace\Python\WebTesting\util
        log_dir = os.path.join('../logs')
        # 日志名称构建
        log_file_name = datetime.now().strftime("%Y-%m-%d") + '.log'
        log_file_path = log_dir + '/' + log_file_name
        print(log_file_path)

        # 2.2 好的，将日志写进log文件中
        self.file_handle = logging.FileHandler(log_file_path, 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s %(funcName)s %(levelno)s: [%(levelname)s] ---> %(message)s')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()


if __name__ == "__main__":
    rl = RecordLog()
    log_info = rl.get_log()
    log_info.debug('输出到文件中去')
    rl.close_handle()
