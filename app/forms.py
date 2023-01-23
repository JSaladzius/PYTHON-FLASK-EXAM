from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.db_models.User import User


class LoginForm(FlaskForm):
    email = StringField("Email" , [DataRequired(),Email()])
    password = PasswordField("Password" , [DataRequired()])
    remember = BooleanField('Prisiminti')
    submit = SubmitField('Prisijungti')

class RegistrationForm(FlaskForm):
    name = StringField("Name" , [DataRequired()])
    email = StringField("Email" , [DataRequired()])
    password = PasswordField("Password" , [DataRequired()])
    repeated_password = PasswordField("Repeat password" , [EqualTo('password', "Passwords must match.")])
    submit = SubmitField('Register')

    def check_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is taken')

class JoinGroupForm(FlaskForm):
    group_id = IntegerField('Group ID', [DataRequired()])
    submit = SubmitField('Join')

class AddBillForm(FlaskForm):
    discription = StringField("Discription", [DataRequired()])
    amount = IntegerField('Amount', [DataRequired()])
    submit = SubmitField('Post')



