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

class Logs:
    def __int__(self):
        pass

    def logEnent(self, func, *args, **kwargs):
        """
        日志事件修饰器，通过返回对象产生志信息
        :param: func
        :return:
        """
        @wraps(func)
        def logObject(*args, **kwargs):
            print("aaaa")
            func(*args, **kwargs)
            print("aaaaaf")

        return logObject

