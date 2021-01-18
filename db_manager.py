from pony.orm import *

db = Database()
# MySQL
db.bind(provider='mysql', host='localhost', user='root', passwd='chao', db='masala_main')

class Mas_User(db.Entity):
    id=PrimaryKey(int)
    name=Required(str)
    pwd=Required(str)

db.generate_mapping(create_tables=False)

@db_session
def get_user_by_id(uid):
    return Mas_User[uid]

@db_session
def get_user_by_md5(pwdmd5):
    return select(u for u in Mas_User if u.pwd == pwdmd5).first()