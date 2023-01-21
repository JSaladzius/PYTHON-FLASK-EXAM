from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.db_models.User import User


class LoginForm(FlaskForm):
    email = StringField("Email" , [DataRequired(),Email()])
    password = PasswordField("Password" , [DataRequired()])
    remember = BooleanField('Prisiminti')
    submit = SubmitField('Prisijungti')

class RegistrationForm(FlaskForm):
    name = StringField("Name" , [DataRequired()])
    e_mail = StringField("Email" , [DataRequired()])
    password = PasswordField("Password" , [DataRequired()])
    repeated_password = PasswordField("Repeat password" , [EqualTo('password', "Passwords must match.")])
    submit = SubmitField('Register')

    def check_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken')



