# Importar las librerias
from flask import Flask, jsonify, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from .database import db

class Usuario(UserMixin, db.Model):
    __tablename__ = 'usuario'
    # main data
    email = db.Column(db.String(50), primary_key = True)
    username = db.Column(db.String(30), unique=True)
    password_hashed = db.Column(db.String(128), nullable=False)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password_hashed = password
        
    
    @property
    def password(self):
        raise AttributeError('Password is not readable')

    def check_password(self,password):
        return self.password_hashed == password
    
    def get_id(self):
        return (self.email)

    def __repr__(self) -> str:
        return f'e: {self.email} \tu: {self.username} \tg: {self.github}'

class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer(), primary_key=True)
    nombre = db.Column(db.String(), nullable = False)
    apellido = db.Column(db.String(), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    ciclo = db.Column(db.Integer, nullable = False)
    carrera = db.Column(db.String(), nullable = False)
    id_usuario = db.Column(db.String(50), db.ForeignKey('usuario.email'), nullable=True)

    usuario = db.relationship("Usuario", backref="personas")    
    def __repr__(self):
        response = {}
        response['Nombre'] = self.nombre 
        response['usuario'] = self.id_usuario 
        response['apellido'] = self.apellido 
        response['edad'] = self.edad 
        response['ciclo'] = self.ciclo 
        response['carrera'] = self.carrera 
        return response

#db.create_all() #Crea las tablas 
#Rutas de la pagina