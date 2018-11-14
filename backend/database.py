from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import  relationship
from sqlalchemy import ForeignKey

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(32))
    email = db.Column(db.String(255), unique=True, nullable=True)
    phone = db.Column(db.String(15), nullable=True)
    blog = relationship('Blog', backref='user')

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


class Blog_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    create_time = db.Column(db.String(80))
    lead = db.Column(db.String(80))
    remark = db.Column(db.Text)
    total = db.Column(db.Integer)
    blog = relationship('Blog', backref = 'blog_type')

    """博文类型类"""
    def __init__(self, title, create_time=None, lead=None,remark=None ,total=0):
        self.title = title
        if create_time is None:
            create_time = datetime.now()
        self.create_time = create_time
        self.lead = lead
        self.remark  = remark
        self.total = total
    
    def __repr__(self):
        return '<Blog_type {0}>'.format(self.title)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'create_time': self.create_time,
            'lead': self.lead,
            'remark': self.remark,
            'total': self.total
        }


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    author = db.Column(db.String(80))
    content = db.Column(db.Text)
    write_time = db.Column(db.String(80))
    remark = db.Column(db.String(255))
    words_number = db.Column(db.Integer)
    type_id = db.Column(db.Integer, ForeignKey('blog_type.id'))
    user_id = db.Column(db.Integer, ForeignKey('user.id'))

    """博文类型类"""
    def __init__(self, title, content=None, author=None, write_time=None,remark=None ,words_number=0):
        self.title = title
        if author is None:
            author = '佚名'
        self.author = author
        if write_time is None:
            write_time = datetime.now()
        self.content = content
        self.remark = remark
        self.words_number = words_number
    
    def __repr__(self):
        return '<Blog {0}>'.format(self.title)

    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'author' : self.author,
            'content' : self.content,
            'write_time' : self.write_time,
            'remark' : self.remark,
            'words_number' : self.words_number,
            'type_id':self.type_id,
            'user_id':self.user_id
        }
        