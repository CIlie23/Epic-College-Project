#store database models
from werkzeug.security import generate_password_hash, check_password_hash
from . import db #import db object from __init__
from flask_login import UserMixin #gives user obj stuff from flasklogin
#from sqlalchemy import func #automatically add the date

class Note(db.Model): #change to store player score
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    #date = db.Column(db.DateTime(timezone=true), default=func.now())
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #1:24:00
    
class User(db.Model, UserMixin): 
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)# you MUST specify how long the string should be
    password = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150))
    role = db.Column(db.String(50), default='member')
    highest_score = db.Column(db.Integer, default=0)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def update_password(self, new_password):
        self.password = generate_password_hash(new_password, method='scrypt')
        db.session.commit()
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    #notes = db.relationship('Note) access the class Note