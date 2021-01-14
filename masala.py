from flask import Flask, render_template, url_for,request, Response
from flask_login import LoginManager, login_required, login_user, logout_user

from models import AuthModel

app=Flask(__name__)
app.secret_key=r'masala'

login_manager=LoginManager(app)

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