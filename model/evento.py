from sqlalchemy import Column, String, DateTime, Integer
from model.entity_base import Base
from datetime import datetime
from typing import Union

class Evento(Base):
    __tablename__ = 'eventos'
    id = Column(Integer, autoincrement=True, primary_key=True)
    nome = Column(String(150), nullable=False)
    descricao = Column(String(500), nullable=False)
    local = Column(String(100), nullable=False)
    data = Column(DateTime, nullable=False)
    vagas = Column(Integer, nullable=False)

    
    def __init__(self, nome:str, descricao:str, local:str, data:Union[DateTime, None], vagas:int):
        self.nome = nome
        self.descricao = descricao
        self.local = local
        self.data = data
        self.vagas = vagas