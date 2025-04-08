from sqlalchemy.ext.declarative import as_declarative, declarative_base, declared_attr
from sqlalchemy import Column, Integer

@as_declarative()
class EntityBase:
    id = Column(Integer, primary_key=True, autoincrement=True)

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()
    