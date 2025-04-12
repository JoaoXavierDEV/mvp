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

    def __init__(self, nome: str, descricao: str, local: str, data: Union[datetime, None], vagas: int):
        if not nome:
            raise ValueError("O campo 'nome' é obrigatório.")
        if not descricao:
            raise ValueError("O campo 'descricao' é obrigatório.")
        if not local:
            raise ValueError("O campo 'local' é obrigatório.")
        if not data:
            raise ValueError("O campo 'data' é obrigatório.")
        if vagas is None:
            raise ValueError("O campo 'vagas' é obrigatório.")

        self.nome = nome
        self.descricao = descricao
        self.local = local
        self.data = data
        self.vagas = vagas