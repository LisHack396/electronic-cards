from datetime import datetime
from sqlalchemy import Column, String, Float, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Transaction(Base):
    """Modelo de la tabla Transaction"""
    __tablename__ = 'transaction'
    id_trans = Column(Integer(), primary_key=True, autoincrement='auto')
    ser_ref = Column(String(100), nullable=False)
    period = Column(Float(10), nullable=False)
    data_value = Column(Float(10), nullable=False)
    status = Column(String(10), nullable=False, default='F')
    units = Column(Integer(), nullable=True, default='Dollars')
    magnitude = Column(Integer(), nullable=True)
    subject = Column(String(100), nullable=True, default='Electronic Card Transactions (ANZSIC06) - ECT')
    group = Column(String(100), nullable=True)
    series_title_1 = Column(Text, nullable=True, default='Actual')
    series_title_2 = Column(Text(), nullable=True)
    created_on = Column(DateTime(), default=datetime.now())
    update_on = Column(DateTime(), onupdate=datetime.now())
