# region Imports
from flask import Flask, request, send_from_directory, render_template, jsonify, redirect
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from model import db_url
from model.entity_base import Base
from Dto import *
from datetime import datetime 

from model.inscricao import Inscricao
from model.pessoa import Pessoa
from model.evento import Evento

from flask_openapi3 import OpenAPI, Info, Tag
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.error import ErrorSchema
from schemas.inscricao import *
from schemas.pessoa import *
from schemas.evento import EventoSchema, exibir_evento, listar_eventos
from flask_cors import CORS
# endregion

engine = create_engine(db_url)

Session = scoped_session(sessionmaker(bind=engine))

Base.metadata.bind = engine

info = Info(title="Evento API", version="1.0.0", description="Api para cadastro e inscrição de eventos")
app = OpenAPI(__name__, info=info)
CORS(app,resources={r"/*": {"origins": "*"}})

# region definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
inscricao_tag = Tag(name="Inscrição", description="Adição, visualização e remoção de inscrições à base")
cadEvento_tag = Tag(name="Cadastro de Evento", description="Adição e visualização de eventos à base")
listEventos_tag = Tag(name="Lista de Eventos", description="Visualização de todos os eventos cadastratos à base")
participantesEvento_tag = Tag(name="Lista de eventos por pessoa", description="Visualização de eventos cadastrados por pessoa")
# endregion

@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')

@app.post('/inscricao', tags=[inscricao_tag], responses={"200": InscricaoViewSchema, "400": ErrorSchema, "409": ErrorSchema, "404": ErrorSchema })
def inscrever(form: InscricaoSchema):

    try:
        dto = InscricaoDTO(nome= form.nome, email=form.email,evento=form.evento, dataNascimento=form.dataNascimento)
    except Exception as err:
       return {"mesage": err}, 400

    queryEvento:int = dto.evento
    evento = Evento.query.get(queryEvento)
    if not evento:
        return {"error": "Evento não encontrado"}, 404
    
    total_inscricoes = Inscricao.query.filter_by(evento_id=evento.id).count()
    if total_inscricoes >= evento.vagas:
        return {"error": "Não há vagas disponíveis para este evento"}, 400

    pessoa = Pessoa.query.filter_by(nome=dto.nome).first()
    if not pessoa:
        pessoa = Pessoa(nome=dto.nome, data=dto.dataNascimento)
        Session.add(pessoa)
        Session.commit()

    inscricao = Inscricao(pessoa_id=pessoa.id, evento_id=evento.id, email=dto.email, data=datetime.now())
    Session.add(inscricao)
    Session.commit()

    dto.evento = evento.nome

    return exibir_incricao(dto, evento), 200

@app.post('/cadastrarEvento', tags=[cadEvento_tag], responses={"200": EventoSchema, "400": ErrorSchema})
def add_evento(form: EventoSchema):
    try:
        evento = Evento(
            nome= form.nome, 
            descricao=form.descricao,
            local=form.local,
            data=form.data, 
            vagas=form.total_vagas)
        
        Session.add(evento)
        Session.commit()
    except Exception as err:
       return {"error": err}, 400    
    except ValueError as err:
       return {"ValidateException": err}, 400    
    
    return exibir_evento(evento), 201

@app.get('/obterTodosOsEventos', tags=[listEventos_tag], responses={"400": ErrorSchema, "409": ErrorSchema})
def obterTodosOsEventos():
    try:
        eventos = Session.query(Evento).all()

        return listar_eventos(eventos), 200
    except Exception as err:
        return {"error": str(err)}, 500

@app.post('/quantidadeEventosPessoa', tags=[participantesEvento_tag], responses={"200": PessoaViewSchema ,"500": ErrorSchema, "400": ErrorSchema})
def quantidade_eventos_pessoa(form: PessoaSchema):
    """
    Retorna os eventos em que uma pessoa está cadastrada.
    """
    try:

        pessoa = Pessoa.query.filter_by(nome=form.nome).first()
        if not pessoa:
            return {"error": "Pessoa não encontrada"}, 404

        inscricoes = Session.query(Inscricao).filter_by(pessoa_id=pessoa.id).all()

        eventos = []
        for inscricao in inscricoes:
            if hasattr(inscricao, 'evento') and inscricao.evento:  # Verifica se 'evento' existe
                eventos.append({
                    "id": inscricao.evento.id,
                    "nome": inscricao.evento.nome,
                    "descricao": inscricao.evento.descricao,
                    "local": inscricao.evento.local,
                    "data": inscricao.evento.data,
                    "vagas": inscricao.evento.vagas
                })


        return exibir_inscricao(pessoa, form.email, eventos), 200
    except Exception as err:
        return {"error": str(err)}, 500

