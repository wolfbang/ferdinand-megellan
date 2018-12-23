#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : cache_decorator.py
# @Author: lucas
# @Date  : 12/22/18
# @Desc  :


import app.redis_client

from functools import wraps


def cache_deco(expired_time=30L):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            method_name = func.__name__
            key = method_name + ":" + str(args[0])
            result = app.redis_client.get(key)
            if not result:
                result = func(*args, **kwargs)
                app.redis_client.do_set(key, result, expired_time)
                return result
            return result

        return wrapper

    return decorate
