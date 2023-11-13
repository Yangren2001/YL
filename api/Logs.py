# encoding=utf-8

"""
    @Project ：YL 
    @File：Log
    @Time:2023/8/31 11:58
    @Author:YR
    @describe: 日志类

"""
import logging
from api.resource_handle.xmlHandle import XmlHandle
from functools import wraps

class Logs:
    def __int__(self, name="myapp"):
        # 导入日志配置
        # self.log_conf = XmlHandle().read()
        self.logger = logging.getLogger(name)          # 获取日志器对象
        # self.file_handle = logging.FileHandler()

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

