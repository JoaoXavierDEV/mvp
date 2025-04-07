from flask import Flask, request, send_from_directory, render_template
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html"), 200