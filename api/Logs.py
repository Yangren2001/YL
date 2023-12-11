# encoding=utf-8

"""
    @Project ：YL 
    @File：Log
    @Time:2023/8/31 11:58
    @Author:YR
    @describe: 日志类

"""
import logging
from functools import wraps
from api.Config import *


class Logs:

    def __init__(self, name="myapp"):
        """
            日志类
        :param name: 日志器名字，默认myapp
        """
        # 获取日志器对象
        self.logger = logging.getLogger(name)
        self.setLevel()
        # self.file_handle = logging.FileHandler()
        self.stream_handle = logging.StreamHandler()
        self.logger.addHandler(self.stream_handle)
        self.init_log_format()

    def auto_create_log_file(self):
        """
        自动创建日志文件
        :return:
        """
        # 时间检测

    def setLevel(self):
        """
        设置日志等级
        :return:
        """
        level = LOG_LEVEL.upper()
        if hasattr(logging, level):
            self.logger.setLevel(getattr(logging, level))


    def init_log_format(self):
        """
        初始化日志格式
        :return:
        """
        self.stream_handle.setFormatter(logging.Formatter(LOG_OUT_FORMAT, datefmt="%Y-%m-%d %H:%M:%S"))

    def logEnent(self, func, *args, **kwargs):
        """
        日志事件修饰器，通过返回对象产生志信息
        :param: func
        :return:
        """

        @wraps(func)
        def logObject(*args, **kwargs):
            self.logger.info("aaaa")
            func(*args, **kwargs)
            print("aaaaaf")

        return logObject
