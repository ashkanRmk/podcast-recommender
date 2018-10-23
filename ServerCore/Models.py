from flask import Blueprint
from flask_sqlalchemy import *
import json

models = Blueprint('Models', __name__, 'ServerCore')
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(25), nullable=False)
    gender = db.Column(db.Boolean, nullable=False)
    auth = db.Column(db.String(25), unique=True, nullable=True)


@models.route('/install-db')
def intsall():
    # db.create_all()
    User.__table__.create(db.session.bind, checkfirst=True)
    return "db initated"
