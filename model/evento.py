from sqlalchemy import Column, String, DateTime, Integer
from model.entity_base import EntityBase

class Evento(EntityBase):
    data = Column(DateTime)
    local = Column(String)
    descricao = Column(String)
    vagas = Column(Integer)
    nome = Column(String)