from flask import Flask, request, send_from_directory, render_template, jsonify, redirect
#from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from model import db_url
from model.entity_base import Base
from datetime import datetime 

#from model import Session
from model.inscricao import Inscricao
from model.pessoa import Pessoa
from model.evento import Evento
from Dto.InscreverEvento import InscricaoDTO
##
from flask_openapi3 import OpenAPI, Info, Tag
from urllib.parse import unquote
from sqlalchemy.exc import IntegrityError
from logger import logger
from schemas.error import ErrorSchema
from schemas.inscricao import *
from flask_cors import CORS
#

engine = create_engine(db_url)

# Configuração da sessão
Session = scoped_session(sessionmaker(bind=engine))

# Vincular o Base ao engine
Base.metadata.bind = engine

info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# region Eventos

inscricao_tag = Tag(name="Inscrição", description="Adição, visualização e remoção de inscrições à base")
@app.post('/inscricao', tags=[inscricao_tag],
          responses={"200": InscricaoViewSchema, "400": ErrorSchema, "409": ErrorSchema, "404": ErrorSchema })
def inscrever(form: InscricaoSchema):
    # Validar os dados da requisição usando o DTO
    try:
        #data = InscricaoDTO().load(request.json)
        data = InscricaoDTO(nome= form.nome, email=form.email,evento=form.evento_id)
    except Exception as err:
       return {"mesage": err}, 400

    # Verificar se o evento existe
    queryEvento:int = data.evento
    evento = Evento.query.get(queryEvento)
    if not evento:
        return {"error": "Evento não encontrado"}, 404
    
    # Verificar se ainda há vagas no evento
    total_inscricoes = Inscricao.query.filter_by(evento_id=evento.id).count()
    if total_inscricoes >= evento.vagas:
        return {"error": "Não há vagas disponíveis para este evento"}, 400

    # Criar ou encontrar a pessoa
    pessoa = Pessoa.query.filter_by(nome=data.nome).first()
    if not pessoa:
        pessoa = Pessoa(nome=data.nome)
        Session.add(pessoa)
        Session.commit()

    # Criar a inscrição
    inscricao = Inscricao(pessoa_id=pessoa.id, evento_id=evento.id, email=data.email, data=datetime.now())
    Session.add(inscricao)
    Session.commit()

    data.evento = evento.nome

    #return {"message": "Inscrição realizada com sucesso!"}, 201
    return exibir_incricao(data), 200


# endregion