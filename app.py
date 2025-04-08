from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError

from model import Session, EntityBase
from model.evento import Evento
from model.inscricao import Inscricao
from model.pessoa import Pessoa

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html"), 200

@app.route('/favicon.ico')
def favicon():
    return send_from_directory('static', 'favicon.ico', mimetype='image/x-icon')