from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity_base import Base
from datetime import datetime
from typing import Union

class Inscricao(Base):
    __tablename__ = 'inscricoes'
    
    id = Column(Integer, autoincrement=True, primary_key=True)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)
    data = Column(DateTime, nullable=False)
    email = Column(String(50), nullable=False)

    pessoa = relationship('Pessoa', back_populates='inscricoes')
    evento = relationship('Evento')


    def __init__(self, pessoa_id:int, evento_id:int, email:str,
                 data:Union[DateTime, None] = None):
        
        self.pessoa_id = pessoa_id
        self.evento_id = evento_id
        self.email = email

        # se não for informada, será o data exata da inserção no banco
        if data:
            self.data = data