from pony.orm import *
from flask_login import UserMixin
import datetime
import copy

db = Database()
# MySQL
db.bind(provider='mysql', host='localhost', user='root', passwd='chao', db='masala_main')

class Mas_User(db.Entity):
    id=PrimaryKey(int)
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
    height=Optional(str)
    weight=Optional(str)
    register_time=Required(datetime.datetime)
    last_access=Required(datetime.datetime)

db.generate_mapping(create_tables=True)

@db_session
def get_user_by_id(uid):
    return Mas_User[uid]

@db_session
def get_user_by_md5(pwdmd5):
    return select(u for u in Mas_User if u.pwd == pwdmd5).first()

@db_session
def create_user(**reg_info):
    pass