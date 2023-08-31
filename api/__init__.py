# encoding=utf-8

"""
    @Project ：YL 
    @File：__init__.py
    @Time:2023/8/31 11:53
    @Author:YR
    @describe:

"""
import os
import sys

__all__ = [i.replace(".py", "") for i in os.listdir(os.path.dirname(__file__))]
sys.path.append(os.path.dirname(__file__))
sys.path.append(os.path.dirname(__file__).join(os.listdir(os.path.dirname(__file__))))