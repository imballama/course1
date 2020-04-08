from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError



class LoginForm(FlaskForm):
    inn = StringField('inn', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign in')


class RegistrationForm(FlaskForm):
    inn = StringField('inn', validators=[DataRequired()])
    email = StringField('Email', validators= [DataRequired(), Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat password', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Register')

def validate_username(self,inn):
    inn = Store.query.filter_by(inn=inn.data).first()
    if inn:
        raise ValidationError('Store with that inn already exists')


def validate_email(self, email):
    inn = Store.query.filter_by(email=email.data).first()
    if user:
        raise ValidationError('Store with that inn already exists')
