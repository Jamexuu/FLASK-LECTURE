from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators, EmailField, SubmitField

class RegistrationForm(FlaskForm):
    username = StringField('Username', [validators.Length(min=4, max=25)], render_kw={"class": "username"})
    email = EmailField('Email Address', [validators.Length(min=6, max=35)], render_kw={"class": "email"})
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, max=35)], render_kw={"class": "password"})
    confirm = PasswordField('Repeat Password', [validators.DataRequired(), validators.EqualTo('password', message='Passwords must match')],
                            render_kw={"class": "confirm"})

    submit = SubmitField('Submit', render_kw={"class": "submit"})