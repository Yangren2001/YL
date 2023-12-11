# encoding=utf-8

"""
    @Project ：YL 
    @File：Config
    @Time:2023/11/13 16:40
    @Author:YR
    @describe: 初始化配置处理

"""

import os

APP_ROOT_PATH = os.path.abspath(os.path.pardir)   # app根目录
CONFIG_PATH = os.path.join(APP_ROOT_PATH, "api", "Conf")  # 配置文件路径
# 日志配置
"""
debug : 打印全部的日志( notset 等同于 debug )
info : 打印 info, warning, error, critical 级别的日志
warning : 打印 warning, error, critical 级别的日志
error : 打印 error, critical 级别的日志
critical : 打印 critical 级别

format
%(name)s Logger的名字
%(levelname)s 文本形式的日志级别
%(message)s 用户输出的消息
%(asctime)s 字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
%(levelno)s 数字形式的日志级别
%(pathname)s 调用日志输出函数的模块的完整路径名，可能没有
%(filename)s 调用日志输出函数的模块的文件名
%(module)s  调用日志输出函数的模块名
%(funcName)s 调用日志输出函数的函数名
%(lineno)d 调用日志输出函数的语句所在的代码行
%(created)f 当前时间，用UNIX标准的表示时间的浮 点数表示
%(relativeCreated)d 输出日志信息时的，自Logger创建以 来的毫秒数
"""

LOG_LEVEL = "debug"      # 日志等级
LOG_DIR = os.path.join(APP_ROOT_PATH, "logs")         # 日志目录
LOG_SUFFIX = "log"     # 日志后缀
LOG_OUT_FORMAT = "%(asctime)s %(levelname)s: %(message)s"     # 日志格式
