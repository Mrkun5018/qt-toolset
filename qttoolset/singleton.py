#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Project ：mercury-testtool-a1 
@File    ：singleton.py
@Email   ：2220138602@QQ.COM
@Date    ：2024/8/20 10:01 
"""


class QSingleton:
    _instance_table = {}

    def __new__(cls, *args, **kwargs):
        instance = cls._instance_table.get(cls.__name__, None)
        if instance is None:
            instance = super().__new__(cls)
            cls._instance_table[cls.__name__] = instance
            return instance
        else:
            raise RuntimeError(f"Only one instance of {cls.__name__} is allowed, use get_instance() to get the instance.")

    @classmethod
    def get_instance(cls):
        instance = cls._instance_table.get(cls.__name__, None)
        if instance is not None:
            return instance
        raise ValueError("the instance is not initialized.")
