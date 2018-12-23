#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shop_query_with_cache_deco.py
# @Author: lucas
# @Date  : 12/22/18
# @Desc  :

import shop_query
from app.util.cache_decorator import cache_deco


@cache_deco()
def get_by_id(shop_id):
    return shop_query.get(shop_id)


def run():
    shop_id = 65
    shop = get_by_id(shop_id)
    print shop


if __name__ == '__main__':
    run()
