from flask import Blueprint, render_template, request, session
from flask_wtf import FlaskForm
from wtforms import (
    TextAreaField,
    StringField,
    PasswordField,
    validators,
    FileField,
    Form,
    SubmitField
)


class LoginF(Form):
    username = StringField(
                'Username',
                [validators.DataRequired(message = 'Espacio requerido'),
                 validators.length(min = 5, max = 30, message='No es valido')
                ])
    password =  PasswordField(
                 'Password',
                 [validators.DataRequired(message = 'Espacio requerido')]
                )
    
    def __init__(self, *args, **kwargs):
        super(LoginF, self).__init__(*args, **kwargs)

class SignUpF(Form):
    username = StringField(
                'Username',
                [validators.DataRequired(message = 'Espacio requerido'),
                 validators.length(min = 5, max = 30, message='No es valido')
                ])
    email = StringField(
                        'Email',
                        [validators.DataRequired(message= 'Debes colocar un correo')]
                        )
    password =  PasswordField(
                 'Password',
                 [validators.DataRequired(message = 'Espacio requerido')]
                )
              
    def __init__(self, *args, **kwargs):
        super(SignUpF, self).__init__(*args, **kwargs)

class Alumno(Form):
    nombre = StringField(
                'nombre',
                [validators.DataRequired(message = 'Espacio requerido'),
                 validators.length(min = 5, max = 30, message='No es valido')
                ])
    apellido = StringField(
                'apellido',
                [validators.DataRequired(message= 'Debes colocar un correo')]
                )
    edad =  StringField(
                 'edad',
                 [validators.DataRequired(message = 'Espacio requerido')]
                )

    ciclo =  StringField(
                 'ciclo',
                 [validators.DataRequired(message = 'Espacio requerido')]
    )

    carrera =  StringField(
                 'carrera',
                 [validators.DataRequired(message = 'Espacio requerido')]
    )
    def __init__(self, *args, **kwargs):
        super(Alumno, self).__init__(*args, **kwargs)
