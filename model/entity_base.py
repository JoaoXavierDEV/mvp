from sqlalchemy.ext.declarative import as_declarative, declarative_base, declared_attr
from sqlalchemy import Column, Integer

Base = declarative_base()

class EntityBase(Base):
    __abstract__ = True
    id = Column(Integer, autoincrement=True, primary_key=True)

