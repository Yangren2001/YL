# encoding=utf-8

"""
    @Project ：YL 
    @File：HandleBase
    @Time:2023/11/13 11:16
    @Author:YR
    @describe: 处理接口

"""

import abc
import os
# 创建Handle类前处理


# HandleApi
class HandleBase(abc.ABC):
    def __int__(self, *args, **kwargs):
        pass

    @abc.abstractmethod
    def read(self, *args, **kwargs):
        """
        读取数据
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abc.abstractmethod
    def dataReturn(self, *args, **kwargs):
        """
        对读取数据进行格式处理，返回对应数据
        :param args:
        :param kwargs:
        :return:
        """
        pass

    @abc.abstractmethod
    def write(self, *args, **kwargs):
        """
        将数据写入为对应文件类型
        :param args:
        :param kwargs:
        :return:
        """
        pass

    def convertAbsPath(self, path) -> str:
        """
        将路径转化为绝对路径
        :param path:
        :return:
        """
        # 判断路径存在
        if not os.path.exists(path):
            return ''
        # 判断是否为绝对路径
        if not os.path.isabs(path):
            return os.path.abspath(path)
        else:
            return path

