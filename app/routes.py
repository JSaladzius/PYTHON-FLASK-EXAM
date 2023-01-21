from app import app, db, login_manager, bcrypt
from flask_login import current_user ,login_required,login_user
from flask import flash, redirect, render_template, request, url_for
from app.forms import LoginForm , RegistrationForm

from app.db_models.User import User


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


@app.route("/", methods=['GET','POST'])
def home():
    form=LoginForm()
    return render_template("base.html", title="LOG iN", form=form)



@app.route("/login" , methods=['GET','POST'])
def log_in():
    if current_user.is_authenticated:
        return redirect(url_for('groups'))
    form=LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash('Bravo!', "you'r in")
            return redirect(url_for('groups'))
        else:
            flash('No luck. Check email or secret word', 'warning')
    return render_template("login.html", title="LOG iN", form=form)


@app.route("/register" , methods=['GET', 'POST'])
def register():
    db.create_all
    if current_user.is_authenticated:
        return redirect(url_for('groups'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.e_mail.data, password=encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash('Now Joined!', 'Success')
        return redirect(url_for('log_in'))
    return render_template('register.html', form=form)


@app.route("/groups", methods=['GET','POST'])
@login_required
def groups():
    form=LoginForm()
    return render_template("groups.html", title="LOG iN", form=form)

