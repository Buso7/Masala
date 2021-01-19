from pony.orm import *
from flask_login import UserMixin
import datetime
import copy

db = Database()
# MySQL
db.bind(provider='mysql', host='localhost', user='root', passwd='chao', db='masala_main')

class Mas_User(db.Entity):
    id=PrimaryKey(int,auto=True)
    name=Required(str)
    pwd=Required(str)
    email=Required(str)
    gender_id=Required(int)
    birthday=Required(datetime.date)
    age=Optional(int)
    state_id=Required(int)
    edubackground_id=Required(int)
    income_id=Required(int)
    province_id=Optional(int)
    city_id=Optional(int)
    register_time=Required(datetime.datetime)
    last_access=Required(datetime.datetime)
    account_status=Required(int)

db.generate_mapping(create_tables=True)

@db_session
def get_user_by_id(uid):
    return Mas_User[uid]

@db_session
def get_user_by_md5(pwdmd5):
    return select(u for u in Mas_User if u.pwd == pwdmd5).first()

@db_session
def create_user(**reg_info):
    Mas_User(name=reg_info['name']
            ,email=reg_info['email']
            ,pwd=reg_info['pwd']
            ,gender_id=reg_info['gender_id']
            ,birthday=reg_info['birthday']
            ,age=reg_info['age']
            ,state_id=reg_info['state_id']
            ,edubackground_id=reg_info['edubackground_id']
            ,income_id=reg_info['income_id']
            ,province_id=reg_info['province_id']
            ,city_id=reg_info['city_id']
            ,register_time=reg_info['register_time']
            ,last_access=reg_info['last_access']
            ,account_status=reg_info['account_status'])