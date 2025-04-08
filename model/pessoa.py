from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from model.entity_base import EntityBase

class Pessoa(EntityBase):
    nome = Column(String)
    email = Column(String)
    inscricoes = relationship("Inscricao", backref="pessoa")