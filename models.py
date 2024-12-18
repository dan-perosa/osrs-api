from sqlalchemy import Table, String, Column, Integer, DateTime
from db_conn import engine
from sqlalchemy.orm import DeclarativeBase
import datetime


class Base(DeclarativeBase):
    pass

class Quest(Base):
    __table__ = Table(
    "quests",
    Base.metadata,
    autoload_with=engine,
    )
    
class Monster(Base):
    __table__ = Table(
    "monsters",
    Base.metadata,
    autoload_with=engine,
    )
    
class Equipment(Base):
    __table__ = Table(
    "equipments",
    Base.metadata,
    autoload_with=engine,
    )
    
class User(Base):
    __table__ = Table(
    "users",
    Base.metadata,
    autoload_with=engine,
    )
    
    def __init__(self, username, password):
        self.username = username
        self.password = password

