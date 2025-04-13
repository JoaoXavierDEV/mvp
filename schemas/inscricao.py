from typing import Optional, List
from model.inscricao import Inscricao
from model.evento import Evento
from Dto.InscreverEvento import InscricaoDTO
from pydantic import BaseModel, EmailStr
from datetime import datetime

class InscricaoSchema(BaseModel):
    """ Define como um nova inscrição a ser inserido deve ser representado
    """
    nome: str = "André"
    evento: int = 2
    email: str = "andre@outlook"
    dataNascimento: Optional[datetime] = datetime.now()

class InscricaoViewSchema(BaseModel):
    """ Define como uma inscrição será retornado
    """
    id: int = 1
    pessoa_id: int = 1
    evento_id: int = 1
    data: Optional[datetime] = datetime.now()
    email: str = "user@outlook.com"


def exibir_incricao(inscricao: InscricaoDTO, evento: Evento):
    """ Retorna uma representação da inscrição realizada.
    """
    return {
        "nome": inscricao.nome,
        "email": inscricao.email,
        "evento": inscricao.evento,
        "local": evento.local,
    }
