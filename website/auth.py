#authentification stuff
from flask import Blueprint, render_template, request, flash, redirect, url_for
from.models import User
from werkzeug.security import generate_password_hash, check_password_hash #secure password, we dont want to save the password as the password, we need to obfuscate it
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST': #ask for the data from db
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):#ask for password
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password! Try again.', category='error')
        else:
            flash('Email does not exist.', category='error', user=current_user)
                
    return render_template("login.html")# text="testing", boolean=True you can pass variables here which is cool ex.bool=true

@auth.route('/logout')
@login_required #makes sure we can't access unless logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        confirmPassword = request.form.get('confirmPassword')
        
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        
        if len(email) < 4:
            flash('Invalid email', category='error')
            pass
        elif len(username) < 2:
            flash('Username too short!', category='error')
            pass
        elif password != confirmPassword:
            flash('Password don\'t match!', category='error')
            pass
        elif len(password) < 8:
            flash('Parola trebuie sa aiba cel putin 8 caractere!', category='error')
            pass
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password), method='sha256')#hasing algorithm
            db.session.add(new_user) #we need to add this so the user is added
            db.session.commit() #update the database
            login_user(user, remember=True)
            flash('Cont creat !', category='success')
            return redirect(url_for('views.home')) #we can use /home but it's better to use that so if we ever change the home page it will automaticall change
            pass

    return render_template("sign_up.html", user=current_user)

@auth.route('/terms-of-service')
def tos():
    return render_template("TOS.html")

@auth.route('/account-issues')
def account_issues():
    return render_template("issues.html")