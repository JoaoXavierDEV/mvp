from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model.entity_base import EntityBase

class Pessoa(EntityBase):
    __tablename__ = 'pessoas'

    nome = Column(String, nullable=False)
    dataNascimento = Column(DateTime, nullable=True)
    inscricoes = relationship('Inscricao', back_populates='pessoa', cascade='all, delete-orphan')
