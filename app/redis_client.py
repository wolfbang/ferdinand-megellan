#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : redis_client.py
# @Author: lucas
# @Date  : 12/21/18
# @Desc  :


import redis
import logging

from shop_query import generate_number_string

from pprint import pprint

logging.basicConfig(filename=u'/Users/lucas/projects/ferdinand-magellan/redis-logger.log', filemode="a+",
                    level=logging.DEBUG)
client = redis.Redis(host=u'localhost', port=6379, db=0)


def do_set(key=None, value=None, expired=20000L):
    if not key:
        return
    result = client.set(key, value)
    client.expire(key, expired)
    return result


def get(key=None):
    if not key:
        return
    value = client.get(key)
    return value


def delete(key=None):
    if not key:
        return
    return client.delete(key)


def hmset(key=None, map={}):
    if not key:
        return
    return client.hmset(key, map)


def hmget(key=None):
    if not key:
        return

    return client.hgetall(key)


def run():
    key = "ferdinand:magellan"
    value = "magellan" + "-" + generate_number_string(16)
    pprint(do_set(key, value))
    pprint(get(key))
    pprint(delete(key))

    key = "magellan:SM:ferdinand:magellan"
    mapping = {
        "name": "magellan",
        "phone": generate_number_string(13)
    }

    pprint(hmset(key, mapping))
    pprint(hmget(key))


if __name__ == '__main__':
    run()
