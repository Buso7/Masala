from flask import Flask, render_template, url_for,request,redirect,flash
from flask_login import login_required, login_user, logout_user
from flask_wtf.csrf import CSRFProtect
import hashlib
from flask_socketio import SocketIO
from datetime import date,datetime

from auth import login_manager,AuthModel
from db_manager import get_user_by_id,get_user_by_md5,Mas_User,create_user
from flask_avatars import Avatars

app=Flask(__name__)
app.secret_key=r'masala'

login_manager.init_app(app)
csrf = CSRFProtect(app)
avatar = Avatars(app)

@login_manager.user_loader
def load_user(id):
    mu =  get_user_by_id(id)
    au = AuthModel(mu.id)
    au.name=mu.name
    return au

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
            m_user = AuthModel(u.id)
            m_user.name=u.name
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
        args = {
        'name' : request.form['name'],
        'email' : request.form['email'],
        'pwd' : hashlib.md5((request.form['name']+request.form['pwd']).encode()).hexdigest(),
        'gender_id' : request.form['gender_id'],
        'birthday' : request.form['birthday'],
        'age' : datetime.now().date().year - datetime.strptime(request.form['birthday'],'%Y-%m-%d').date().year,
        'state_id' : request.form['state_id'],
        'edubackground_id' : request.form['edubackground_id'],
        'income_id' : request.form['income_id'],
        'province_id' : request.form['province_id'],
        'city_id' : request.form['city_id'],
        'register_time' : datetime.now(),
        'last_access' : datetime.now(),
        'account_status' : 0}
        create_user(**args)
    return redirect('register')

@app.route('/gen_avatar',methods=['GET'])
def gen_avatar():
    txt = request.args['txt']
    return avatar.robohash(txt)