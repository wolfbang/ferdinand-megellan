#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : shop_query.py
# @Author: lucas
# @Date  : 12/19/18
# @Desc  :

from app.db.models import Shop

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


# dev
engine = create_engine('mysql+pymysql://root:12345678@localhost:3306/magellan')
DBSession = sessionmaker(bind=engine)


def query(size):
    session = DBSession()
    shops = session.query(Shop).filter(Shop.id > 0).limit(size).all()
    return shops


def run():
    shops = query(50)
    if not shops:
        return
    for shop in shops:
        from pprint import pprint
        pprint(str(shop.__dict__))


if __name__ == '__main__':
    run()
