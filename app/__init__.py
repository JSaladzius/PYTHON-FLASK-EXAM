import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt

base_dir = os.path.dirname(__file__)

app = Flask(__name__)
app.app_context().push()
app.config.from_prefixed_env()

# app.config['SECRET_KEY'] = 'q6xkrCHWTnGxwCk87jrFrHyqE7Pj9yjq'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'splitbill.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.db')


db = SQLAlchemy(app)
db.create_all()
login_manager = LoginManager(app)
bcrypt = Bcrypt(app)
mail = Mail(app)


# from app.db_models import Debt
from app import routes