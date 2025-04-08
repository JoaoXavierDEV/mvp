from sqlalchemy import Column, String, DateTime, Integer
from model.entity_base import EntityBase

class Evento(EntityBase):
    __tablename__ = 'eventos'

    nome = Column(String, nullable=False)
    descricao = Column(String, nullable=False)
    local = Column(String, nullable=False)
    data = Column(DateTime, nullable=False)
    vagas = Column(Integer, nullable=False)