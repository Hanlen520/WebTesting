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


if __name__ == "__main__":
    rl = RecordLog()
