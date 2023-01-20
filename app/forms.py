from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email



class LoginForm(FlaskForm):
    email = StringField("Email" , [DataRequired(),Email()])
    password = PasswordField("Password" , [DataRequired()])
    remember = BooleanField('Prisiminti')
    submit = SubmitField('Prisijungti')
