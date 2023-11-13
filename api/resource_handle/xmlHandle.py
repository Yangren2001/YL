# encoding=utf-8

"""
    @Project ：YL 
    @File：xmlHandle
    @Time:2023/11/13 11:31
    @Author:YR
    @describe:xml文件处理

"""

import api.resource_handle.HandleBase as HandleBase
from lxml import etree

class XmlHandle(HandleBase.HandleBase):
    """
    xml文件处理
    """

    def read(self, path, *args, **kwargs) -> dict:
        """
        读取xml数据
        :param path: 路径
        :param args:
        :param kwargs:
        :return: dict
        """
        tree = etree.parse(path).getroot()  # 获取xml树
        return self.dataReturn(tree)

    def dataReturn(self, data, *args, **kwargs) -> dict:
        """
        对数据进行处理，返回特定格式
        :param data:
        :param args:
        :param kwargs:
        :return: dict
        """
        attr_names = data.xpath("property/name/text()")
        attr_values = data.xpath("property/value/text()")
        return dict(zip(attr_names, attr_values))

    def write(self, *args, **kwargs):
        pass