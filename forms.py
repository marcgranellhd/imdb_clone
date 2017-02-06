from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email

class User(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired('Debe introducir un correo electronico'), Email('El formato de su correo no es correcto')])
    password1 = PasswordField('Password', validators=[DataRequired('Debe introducir una contraseña')])
    password2 = PasswordField('Repita la contraseña', validators=[DataRequired('Debe introducir la contraseña de nuevo')])

    submit = SubmitField('Registrarme')