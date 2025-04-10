from typing import Optional, List
from model.inscricao import Inscricao
from Dto.InscreverEvento import InscricaoDTO
from pydantic import BaseModel, EmailStr
from datetime import datetime

class InscricaoSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    nome: str
    data: Optional[datetime]
    evento_id: int
    email: str
# Permite que o Pydantic converta objetos ORM (como os retornados pelo SQLAlchemy) em schemas Pydantic.
    class Config:
        orm_mode = True

class InscricaoViewSchema(BaseModel):
    """ Define como um produto será retornado: produto + comentários.
    """
    id: int = 1
    pessoa_id: int = 1
    evento_id: int = 1
    data: Optional[datetime] = datetime.now()
    email: str = "user@outlook.com"


def exibir_incricao(inscricao: InscricaoDTO):
    """ Retorna uma representação da inscrição realizada.
    """
    return {
        "nome": inscricao.nome,
        "email": inscricao.email,
        "evento": inscricao.evento,
        "dataNascimento": inscricao.dataNascimento,
    }
