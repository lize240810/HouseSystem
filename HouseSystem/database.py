from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(255), unique=True, nullable=True)
    phone = db.Column(db.String(15), nullable=True)

    def __init__(self, username, password, email=None, phone=None):
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        
    def __repr__(self):
        return '<User %r>' % self.username

    def to_dict(self):
        return {
            'id' :self.id,
            'username' :self.username,
            'email' :self.email,
            'phone' :self.phone
        }