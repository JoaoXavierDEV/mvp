from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy.orm import relationship
from model.entity_base import EntityBase

class Inscricao(EntityBase):
    __tablename__ = 'inscricoes'

    pessoa_id = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    evento_id = Column(Integer, ForeignKey('eventos.id'), nullable=False)
    data = Column(DateTime, nullable=False)
    email = Column(String, nullable=False)

    pessoa = relationship('Pessoa', back_populates='inscricoes')
    evento = relationship('Evento')