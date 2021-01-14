from flask_login import UserMixin

class AuthModel(UserMixin):
    def __ini__(self, id=None):
        self.id = id