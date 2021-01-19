from flask import Flask, render_template, url_for,request,redirect,flash
from flask_login import login_required, login_user, logout_user
from flask_wtf.csrf import CSRFProtect
import hashlib
from flask_socketio import SocketIO
from datetime import date,datetime

from auth import login_manager
from db_manager import get_user_by_id,get_user_by_md5,Mas_User

app=Flask(__name__)
app.secret_key=r'masala'

login_manager.init_app(app)
csrf = CSRFProtect(app)

@login_manager.user_loader
def load_user(id):
    return get_user_by_id(id)

@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET','POST'])
def login():
    if request.method == 'GET':
        flash(None)
        return render_template('login.html')
    if request.method == 'POST':
        try:
            reme = request.form['reme']
        except KeyError:
            reme = False
        name = request.form['name']
        pwd = request.form['pwd']
        pwd_md5 = hashlib.md5((name+pwd).encode())
        u = get_user_by_md5(pwd_md5.hexdigest())
        if u is not None:
            m_user = AuthModel()
            m_user.id=u.id
            login_user(m_user,reme)
            return redirect('/')
        flash('用户名或密码错误','login')
        return redirect('login')
    return redirect('login')

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')

@app.route('/register',methods=['GET','POST'])
def register():
    if request.method=='GET':
        return render_template('register.html')
    if request.method=='POST':
        #必填
        name = request.form['name']
        email = request.form['email']
        pwd = request.form['pwd']
        pwd2 = request.form['pwd2']
        gender_id=request.form['gender_id']
        birthday = request.form['birthday']
        state_id = request.form['state']
        edubackground_id = request.form['edubackground_id']
        income_id = request.form['income_id']
        province_id = request.form['province']
        city_id = request.form['city']
        height = request['height']
        weight = request['weight']
        register_time = datetime.now()
        last_access = datetime.now()
        return 'ok'
    return None
