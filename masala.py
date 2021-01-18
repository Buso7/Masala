from flask import Flask, render_template, url_for,request, Response,redirect
from flask_login import login_required, login_user, logout_user
from flask_wtf.csrf import CSRFProtect

from auth import login_manager
from models import AuthModel

app=Flask(__name__)
app.secret_key=r'masala'

login_manager.init_app(app)
csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(id):
    u = AuthModel()
    u.id=1
    return u

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        u = AuthModel()
        u.id='1'
        login_user(u)
        return redirect('/')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/register')
def register():
    pass