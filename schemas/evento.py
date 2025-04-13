from typing import Optional, List, Union
from model.inscricao import Inscricao
from model.evento import Evento
from Dto.InscreverEvento import InscricaoDTO
from pydantic import BaseModel, EmailStr
from datetime import datetime, date,timedelta


class EventoSchema(BaseModel):
    """ Define como um nova inscrição a ser inserida deve ser representada
    """
    #nome: Optional[str]= "Desenvolvimento C#"
    nome: str= "Desenvolvimento C#"
    descricao: str = "Construção de API Rest"
    local: str = "Sala 506"
    data: datetime = datetime.now() + timedelta(weeks=5)
    total_vagas: int = 50



class EventoViewSchema(BaseModel):
    """ Define como uma inscrição será retornado
    """
    nome: str = ".NET 8"
    descricao: str = "Apresentação das tecnologias da Microsoft"
    local: str = "Sala 209"
    data: Optional[datetime] = datetime.now()
    total_vagas: int = 20


def exibir_evento(evento: Evento):
    """ Retorna uma representação da inscrição realizada.
    """
    return {
        "nome": evento.nome,
        "descricao": evento.descricao,
        "local" : evento.local,
        "data": evento.data,
        "Total Vagas": evento.vagas,
    }


def listar_eventos(eventos: List[Evento]):
    """ Retorna uma lista de eventos no formato esperado.
    """
    return [
        {
            "id": evento.id,
            "nome": evento.nome,
            "descricao": evento.descricao,
            "local": evento.local,
            "data": evento.data,
            "total_vagas": evento.vagas,
        }
        for evento in eventos
    ]
