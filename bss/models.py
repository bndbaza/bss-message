from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Entry(Base):
    __tablename__ = 'Entry'
    Id = Column(Integer, primary_key=True)
    RegNumber = Column(String(15),)
    Date = Column(Date)
    Organ = Column(String(100))
    Address = Column(String(100))
    Content = Column(String(500))
    Sender = Column(String(200))
    Wey = Column(String(200))
