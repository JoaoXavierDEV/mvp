from sqlalchemy import Column, String, DateTime, Integer
from model.entity_base import EntityBase

class Inscricao(EntityBase):
    nome = Column(String)
    data = Column(DateTime)
    email = Column(String)
    pessoa = Column