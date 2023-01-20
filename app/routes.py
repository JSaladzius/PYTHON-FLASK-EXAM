from app import app, db, login_manager
from flask_login import current_user
from flask import flash, redirect, render_template, request, url_for
from app.forms import LoginForm

from app.db_models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# @app.route("/")
# def index():
#     return render_template("login.html")

@app.route("/", methods=['GET','POST'])
def log_in():
    form=LoginForm()
    return render_template("login.html", title="LOG iN", form=form)


# @app.route("/login" , methods=['GET','POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('login'))
#     form=LoginForm()
#     if request.method == 'POST' and form.validate_on_submit():