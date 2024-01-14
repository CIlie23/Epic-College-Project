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
                #flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                #flash('Incorrect password! Try again.', category='error')
                print('incorrect password')
        else:
            #flash('Email does not exist.', category='error', user=current_user)
            print('unknown email')
                
    return render_template("login.html", user=current_user)# text="testing", boolean=True you can pass variables here which is cool ex.bool=true

@auth.route('/logout')
@login_required #makes sure we can't access unless logged in
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
    

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('firstName')
        password = request.form.get('password')
        passwordConfirm = request.form.get('passwordConfirm')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(username) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password != passwordConfirm:
            flash('Passwords don\'t match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password, method='scrypt'), role='member')
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/change-password', methods=['GET', 'POST'])
@login_required
def change_password():
    if request.method == 'POST':
        current_password = request.form.get('current_password')
        new_password = request.form.get('new_password')
        confirm_password = request.form.get('confirm_password')

        user = current_user

        # Validate the current password
        if not user.check_password(current_password):
            flash('Incorrect current password. Password not changed.', category='error')
            return redirect(url_for('auth.change_password'))

        # Validate the new password and confirmation
        if len(new_password) < 7:
            flash('Password must be at least 7 characters.', category='error')
            return redirect(url_for('auth.change_password'))
        elif new_password != confirm_password:
            flash('Passwords do not match.', category='error')
            return redirect(url_for('auth.change_password'))

        # Update the password
        user.update_password(new_password)
        flash('Password changed successfully.', category='success')
        return redirect(url_for('.login'))  # Redirect to a suitable view after password change

    return render_template('changepass.html')

@auth.route('/delete-account', methods=['POST'])
@login_required
def delete_account():
    if request.method == 'POST':
        user = current_user
        user.delete()
        logout_user()  
        flash('Account deleted successfully.', category='success')
        return redirect(url_for('.sign_up')) 

@auth.route('/terms-of-service')
def tos():
    return render_template("TOS.html")

@auth.route('/account-issues')
def account_issues():
    return render_template("issues.html")

def get_all_users():
    users = User.query.all()
    return users

@auth.route('/profile')
@login_required
def user_profile():
    users = get_all_users()
    return render_template("profile.html", users=users, user=current_user)

@auth.route('/save_score/<int:nivel>') #i am killing myself
@login_required
def save_score(nivel):
    print(f"Score received: {nivel}")
    if nivel > current_user.highest_score:
        current_user.highest_score = nivel
        db.session.commit()
        print("Score saved successfully.")
    else:
        print("Score not higher than current highest score.")
    return redirect(url_for('views.home'))

