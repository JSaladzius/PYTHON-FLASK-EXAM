from app import app, db, login_manager, bcrypt
from flask_login import current_user ,login_required,login_user,logout_user
from flask import flash, redirect, render_template, request, url_for, session
from app.forms import LoginForm , RegistrationForm , AddBillForm , JoinGroupForm
# from flask_authorize.plugin import Authorizer
# from flask_authorize import RestrictionsMixin, AllowancesMixin , PermissionsMixin, Authorize
# from flask import jsonify
from app.db_models.Group import user_group


from app.db_models.User import User
from app.db_models.Group import Group
from app.db_models.Bill import GroupBill


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
            return redirect(url_for('groups'))
        else:
            flash('No luck. Check email or secret word', 'warning')
    return render_template("login.html", title="LOG iN", form=form)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/register" , methods=['GET', 'POST'])
def register():
    db.create_all
    if current_user.is_authenticated:
        return redirect(url_for('groups'))
    form = RegistrationForm()
    if request.method == 'POST' and form.validate_on_submit():
        encrypted_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name = form.name.data, email = form.email.data, password = encrypted_password)
        db.session.add(user)
        db.session.commit()
        flash('Now Joined!', 'success')
        return redirect(url_for('log_in'))
    return render_template('register.html', form=form)


@app.route("/groups", methods=['GET','POST'])
@login_required
def groups():
    
    user_id = current_user.id
    user = User.query.get(user_id)
    groups_f = user.groups

    form = JoinGroupForm()
    if form.validate_on_submit():
        group_id = request.form.get("group_id")
        group_id = int(group_id)
        print(type(group_id))
        group = Group.query.filter_by(id=group_id).first()
        print(group)
        if not group:
            print ("Group not found", 404)
            flash('Group not found', 'warning')

        else:
            is_in_group = group_id in [group.id for group in user.groups]
            g = group.id
            g = str(g)
            if is_in_group:
                
                print('Allready in group', g)
                flash('Allready in group' + ' ' + g )
            else:
                user.groups.append(group)
                db.session.commit()
                print ("User added to group")
                flash('Joined group '+ ' ' + g )
                return redirect(url_for('groups'))
   
    return render_template("groups.html", title="GROUPS" , groups=groups_f , form=form)

        

@app.route("/bills/<int:group_id>", methods=['GET','POST'])
@login_required
def bills(group_id):
    session['selected_group_id'] = group_id
    form = AddBillForm()
    bills = GroupBill.query.filter_by(id_group=group_id).all()
    return render_template("bills.html", title="BILLS" ,form=form, bills = bills, id_group = group_id)
    

@app.route('/bills', methods=['POST'])
def add_bill():
    group_id = session.get('selected_group_id')

    form = AddBillForm()
    bills = GroupBill.query.filter_by(id_group=group_id).all()
    if request.method == 'POST' and form.validate_on_submit():
        bill = GroupBill(discription = form.discription.data, amount = form.amount.data, id_group =group_id)
        db.session.add(bill)
        db.session.commit()
        flash('Bill added')    
    return redirect(url_for('bills', group_id=group_id))


