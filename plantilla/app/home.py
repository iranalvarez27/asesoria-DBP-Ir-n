from http import client
import os
from os import access, getenv
from unicodedata import name
from flask import (
    Blueprint,
    Flask,
    flash,
    abort,
    jsonify,
    render_template, 
    redirect, 
    session, 
    url_for, 
    request
)
from flask_login import (
    LoginManager, 
    UserMixin, 
    login_user, 
    login_required,
    current_user
)
import hashlib
from itsdangerous import SignatureExpired, URLSafeTimedSerializer
from .db.database import db

from . import forms 
from .db.models import Persona, Usuario
from werkzeug.utils import secure_filename

app = Blueprint('login', __name__, 
                template_folder='templates')  

def init_login(app):
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_email):
        return Usuario.query.get(user_email)

@app.route('/', methods=['GET'])
def index():
    return render_template('Inicio.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

@app.route('/sign-up/', methods=['GET', 'POST'])
def signup():
    form = forms.SignUpF(request.form)
    return render_template('signup.html', form = form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = forms.LoginF(request.form)

    return render_template("login.html", form=form)

@app.route('/inicio',methods = ['GET', 'POST'])
@login_required
def inicio():
    form = forms.Alumno(request.form)
    
    return render_template('index.html', form = form)

@app.route('/show-data/<user>', methods=['GET'])
@login_required
def agregar(user):
    response = {}
    
    return jsonify(response)

@app.route('/actualizar/<int:id>', methods=['PATCH'])
@login_required
def actualizar(id):
    return 0

@app.route('/delete/<int:id>', methods=['DELETE'])
@login_required
def eliminar(id):
    return 0