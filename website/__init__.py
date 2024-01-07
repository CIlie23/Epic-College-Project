#makes this website folder a python package

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__) #name of the file that was ran, init flask
    app.config['SECRET_KEY'] = 'sdjofjsdfjsdvnsvronvonv' #secure cookie data do not share (shush)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)  
    
    from .views import views
    from .auth import auth
    from flask_login import LoginManager

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/') #lasam asa fara prefix

    from .models import User, Note
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) #checks for the primary key
    
    create_database(app) #call the function
    
    return app

def create_database(app): #checks if the database exists, if not it makes it
    if not path.exists('instance/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

