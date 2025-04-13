from typing import Optional, List
from model.inscricao import Inscricao
from model.evento import Evento
from Dto.InscreverEvento import InscricaoDTO
from pydantic import BaseModel, EmailStr
from datetime import datetime

from model.pessoa import Pessoa
from schemas.evento import *


class PessoaSchema(BaseModel):
    """ Define como uma Pessoa será buscada na API
    """
    nome: str = "João Fernando Moura Xavier"
    email: str = "joao_jfmx@outlook.com"

class PessoaViewSchema(BaseModel):
    """ Define como uma inscrição será retornado
    """
    nome: str = ""
    email: str = ""
    eventos: list[EventoSchema]


def exibir_inscricao(pessoa: Pessoa, email: str ,eventos: List[Evento]):
    """ Retorna uma representação da inscrição realizada.
    """

    return {
        "nome": pessoa.nome,
        "email": email,
        "eventos": eventos
    }
