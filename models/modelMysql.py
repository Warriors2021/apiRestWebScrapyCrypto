from config import AppFlask
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

db = AppFlask().db
login_manager = AppFlask().login_manager

class User(UserMixin, db.Model):
    __tablename__ = "users"
    idusers = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(45), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    token_id = db.Column(db.Integer, db.ForeignKey('tokens.id'))
    token = db.relationship('Token', backref='user', uselist=False)



    def __repr__(self):
        return '<User %r>' % self.name

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return str(self.idusers)

@login_manager.user_loader
def load_user(idusers):
    return User.query.get(int(idusers))

class Token(db.Model):
    __tablename__ = 'tokens'
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(500), nullable=False)
