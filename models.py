from app import db, session, Base
from sqlalchemy.orm import relationship
from flask_jwt_extended import create_access_token
from datetime import timedelta
from passlib.hash import pbkdf2_sha256



class User(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    password = db.Column(db.String(200), nullable=False)
    link = relationship('Link', backref='user',
                                lazy='dynamic')

    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')
        self.password = pbkdf2_sha256.hash(kwargs.get('password'))

    def get_token(self, expire_time=24):
        expire_delta = timedelta(expire_time)
        token = create_access_token(
            identity=self.id, expires_delta=expire_delta)
        return token

    @classmethod
    def authenticate(cls, email, password):
        user = cls.query.filter(cls.email == email).one()
        if not pbkdf2_sha256.verify(password, user.password):
            raise Exception('Неверное имя пользователя или пароль')
        return user


class Link_type(Base):
    __tablename__ = 'link_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(100), nullable=False, unique=True)
    ink = relationship('Link', backref='link_type',
                       lazy='dynamic')

class Link(Base):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    original = db.Column(db.String(500), nullable=False)
    friendly_link = db.Column(db.String(500), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    type_id = db.Column(db.Integer, db.ForeignKey('link_type.id'))
    counter = db.Column(db.Integer, nullable=True)
    
    
    @classmethod
    def get_original_link(cls, arg, type_query):
        link = ()
        if type_query == "id":
            link = cls.query.filter(cls.id == arg).one()
        else:
            if cls.query.filter(cls.friendly_link == arg).count():
                link = cls.query.filter(cls.friendly_link == arg).one()
        return link
