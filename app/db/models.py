# coding: utf-8
from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, DATETIME, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Shop(Base):
    __tablename__ = 'shop'

    id = Column(BIGINT(20), primary_key=True)
    name = Column(VARCHAR(200), nullable=False, server_default=text("''"))
    phone = Column(VARCHAR(255))
    mobile = Column(VARCHAR(50))
    description = Column(VARCHAR(255))
    created_time = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"))
    updated_time = Column(DATETIME(fsp=3), server_default=text("CURRENT_TIMESTAMP(3)"))
