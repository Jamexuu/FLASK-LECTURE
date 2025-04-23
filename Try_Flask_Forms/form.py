from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = EmailField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, max=35)])
    confirm = PasswordField('Repeat Password', [validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')])

    submit = SubmitField('Submit')