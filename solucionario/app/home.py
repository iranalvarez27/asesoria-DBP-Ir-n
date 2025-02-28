from distutils.errors import PreprocessError
from http import client
import json
import os
from os import access, getenv
from unicodedata import name
from urllib import response
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
    if request.method == 'POST':
        nuevo_usuario = Usuario(form.email.data, 
                                form.username.data, 
                                form.password.data)       

        db.session.add(nuevo_usuario)
        db.session.commit()
        login_user(nuevo_usuario)

        return redirect(url_for('login.inicio'))
        
    elif request.method=='GET':                
        return render_template('signup.html', form = form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = forms.LoginF(request.form)
    if request.method == 'POST':
        username = form.username.data
        password = form.password.data

        usuario =  Usuario.query.filter_by(username = username).first()
        if (usuario is not None and 
            usuario.check_password(password)) : #Entra si el usuario existe, tiene correcta la contraseña y está confirmado
            
            login_user(usuario, remember=True)
            return redirect(url_for('login.inicio'))
        else: 
            print("No entraste :(")
        
        return render_template("login.html", form=form)
    else: 
        return render_template("login.html", form=form)

@app.route('/inicio',methods = ['GET', 'POST'])
@login_required
def inicio():
    form = forms.Alumno(request.form)
    if request.method == 'POST': 
        alumno = Persona(
                    nombre=form.nombre.data,  
                    apellido = form.apellido.data,
                    id_usuario= current_user.email,
                    edad = form.edad.data,
                    ciclo=form.ciclo.data,
                    carrera=form.carrera.data, 
                )
        db.session.add(alumno)  
        db.session.commit()
        subquery = db.session.query(Persona.id).filter(Persona.id_usuario == current_user.email).subquery()
        p = Persona.query.filter(Persona.id.in_(subquery)).order_by('id').all()
    
        if p is not None:
            return redirect('inicio')
        
    subquery = db.session.query(Persona.id).filter(Persona.id_usuario == current_user.email).subquery()
    p = Persona.query.filter(Persona.id.in_(subquery)).order_by('id').all()   
    return render_template('index.html', form = form, cursos = p)

@app.route('/show-data/<user>', methods=['GET'])
@login_required
def agregar(user):
    response = {}
    id = int(user)
    todo = Persona(id=id)
    persona = Persona.query.get(user)
    response['nombre'] = persona.nombre
    response['apellido'] = persona.apellido
    response['edad'] = persona.edad
    response['ciclo'] = persona.ciclo
    response['carrera'] = persona.carrera
    response['user'] = persona.id_usuario
    return jsonify(response)

@app.route('/actualizar/<id>', methods=['GET','POST'])
@login_required
def actualizar(id):
    form = forms.Alumno(request.form)
    if request.method == 'POST':
        persona = Persona.query.filter(Persona.id == id).one_or_none()
        persona.nombre = form.nombre.data
        persona.apellido = form.apellido.data
        persona.edad = int(form.edad.data)
        persona.ciclo = int(form.ciclo.data)
        persona.carrera = form.carrera.data
        db.session.commit()
        return redirect(url_for('login.inicio'))
    return render_template('actualizar.html', form = form, id=id)

@app.route('/delete/<id>', methods=['DELETE'])
@login_required
def eliminar(id):
    response = {}
    try:
        persona = Persona.query.get(id) # 1 registro
        db.session.delete(persona)
        response['id'] = persona.id
        db.session.commit()
        return jsonify(response)
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
        return jsonify(response)
