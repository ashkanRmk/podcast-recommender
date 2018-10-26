from flask import Blueprint
from enum import Enum

models = Blueprint('Models', __name__, 'ServerCore')


class AgeRange(Enum):
    under18 = 0
    f18t24 = 1
    f25t34 = 2
    f35t44 = 3
    f45t54 = 4
    above55 = 5


class User:
    id = None
    gender = None
    age = None
    rating = None

    def __init__(self, id, gender, age, rating):
        self.id = id
        self.gender = gender
        self.age = age
        self.rating = rating


class Rate:
    id = None
    rate = None

    def __init__(self, id, rate):
        self.id = id
        self.rate = rate


class Podcast:
    id = None
    name = None
    desc = None
    main = None
    sub = None

    def __init__(self, id, name, desc, main, sub):
        self.id = id
        self.name = name
        self.desc = desc
        self.main = main
        self.sub = sub


class Subset:
    id = None
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name


from ServerCore.Core import mongo

@models.route('/install-db')
def intsall():
    mongo.db.create_collection("Podcast")
    mongo.db.create_collection("User")
    return "db initated"
