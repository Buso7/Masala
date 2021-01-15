from flask import Flask, render_template, url_for,request, Response
from flask_login import login_required, login_user, logout_user

from auth import login_manager
from models import AuthModel

app=Flask(__name__)
app.secret_key=r'masala'

login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return url_for('/')

@app.route('/logout')
def logout():
    return url_for('/login')

@app.route('/register')
def register():
    pass