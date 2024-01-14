#frontend
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__) #name it views cause is simple

@views.route('/') #what is in home will run
@login_required #now we cannon access this page if we aren't logged in

def home():
   #2:03:00
    #return "<h1>test</h1>" #register in init
   return render_template("home.html", user=current_user) #user=current_user check if user is authenticated
