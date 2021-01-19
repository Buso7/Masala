'''
authentication
'''
from flask_login import LoginManager,UserMixin

login_manager=LoginManager()
login_manager.login_view='login'

class AuthModel(UserMixin):
    def __init__(self,id):
        self.id=id
    name=None