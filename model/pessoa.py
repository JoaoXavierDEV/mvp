from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy.orm import relationship
from model.entity_base import Base
from datetime import datetime
from typing import Union

class Pessoa(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String, nullable=False)
    dataNascimento = Column(DateTime, nullable=True)
    inscricoes = relationship('Inscricao', back_populates='pessoa', cascade='all, delete-orphan')

    def __init__(self, nome:str, data: DateTime):
        self.nome = nome
        self.dataNascimento = data

