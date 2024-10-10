from sqlalchemy import Table
from sqlalchemy import MetaData
from db_conn import engine
from sqlalchemy.orm import DeclarativeBase
import typing
import sqlalchemy as sa

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
    
# quests = Table(
#     'quests',
#     metadata_obj,
#     autoload_with=engine
# )
