#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shop_query.py
# @Author: lucas
# @Date  : 12/19/18
# @Desc  :

from app.db.models import Shop

import random
from random import randint
from pprint import pprint

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import sys
import logging

reload(sys)
sys.setdefaultencoding('utf8')

logging.basicConfig(filename='shop-query.log', filemode='wb',
                    format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# create models with sqlacodegem
# sqlacodegen mysql+pymysql://'root:12345678'@localhost:3306/magellan > app/db/models.py


# dev#charset must be provided
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/magellan?charset=utf8')
DBSession = sessionmaker(bind=engine)


def query(size):
    session = DBSession()
    shops = session.query(Shop).filter(Shop.id > 0).limit(size).all()
    session.close()
    return shops


def get(shop_id):
    session = DBSession()
    shop = session.query(Shop).filter(Shop.id == shop_id).first()
    session.close()
    return shop


def mget(ids):
    session = DBSession()
    shops = session.query(Shop).filter(Shop.id.in_(ids)).all()
    session.close()
    return shops


def add(**shop_create):
    if not shop_create:
        return

    session = DBSession()

    new_shop = Shop()
    for k, v in shop_create.iteritems():
        setattr(new_shop, k, v)

    session.add(new_shop)
    try:
        session.flush()
        shop_id = new_shop.id
        session.commit()
    except Exception as e:
        logger.error('error:{}'.format(e))

    return shop_id


def delete(shop_id):
    if not shop_id:
        return

    session = DBSession()
    result = session.query(Shop).filter(Shop.id == shop_id).delete()
    pprint('delete#result:{}'.format(result))

    try:
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error('error:{}'.format(e))


def update(shop_id, **shop_update):
    if not shop_id:
        raise Exception('shop_id can not be null')

    if not shop_update:
        return

    data = {}
    for k, v in shop_update.items():
        if not (k or v):
            continue
        data[k] = v

    session = DBSession()

    try:
        result = session.query(Shop).filter(Shop.id == shop_id).update(data)
        pprint('update#result:{},{}'.format(shop_id, result))
        session.commit()
    except Exception as e:
        session.rollback()
        logger.error('shop_id:{},error:{}'.format(shop_id, e))


def show_query_shop():
    shops = query(50)
    if not shops:
        return
    for shop in shops:
        from pprint import pprint
        pprint(str(shop.__dict__))
        pprint(str(shop.id))


def get_random_shop_id():
    shops = query(50)
    if not shops:
        return

    random_index = randint(0, len(shops) - 1)
    return shops[random_index].id


def generate_number_string(size):
    import string
    random_string = [random.choice(string.digits) for x in range(0, size)]
    return ''.join(random_string)


def batch():
    show_query_shop()

    pprint(get_random_shop_id())

    shop_id = get_random_shop_id()
    shop = get(shop_id)
    pprint(str(shop.__dict__))

    shop_ids = list()
    shop_id = get_random_shop_id()
    shop_ids.append(shop_id)
    shops = mget(shop_ids)
    pprint(shops)

    random_id = randint(1000000, 9000000)
    name = u'great-shop-' + str(random_id)
    shop_create = {'name': name,
                   'phone': generate_number_string(3) + '-' + generate_number_string(7),
                   'mobile': generate_number_string(11),
                   'description': u'''It's a desc'''}

    pprint(add(**shop_create))

    shop_id = get_random_shop_id()
    delete(shop_id)

    shop_id = get_random_shop_id()
    random_id = randint(1000000, 9000000)
    name = u'great-shop-' + str(random_id)
    shop_update = {'name': name,
                   'phone': generate_number_string(3) + '-' + generate_number_string(7),
                   'mobile': generate_number_string(11),
                   'description': u'''It's a desc'''}

    update(shop_id, **shop_update)
    pprint(get(shop_id))


def run():
    batch()


if __name__ == '__main__':
    run()
