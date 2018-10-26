from enum import Enum

from flask import Blueprint

models = Blueprint('Models', __name__, 'ServerCore')


class AgeRange(Enum):
    Under18 = 0
    F18_T24 = 1
    F25_T34 = 2
    F35_T44 = 3
    F45_T54 = 4
    Above55 = 5


class User:
    id = None
    gender = None
    age = None
    ratings = None

    def __init__(self, id, gender, age, ratings):
        self.id = id
        self.gender = gender
        self.age = age
        self.ratings = ratings


class Rate:
    id = None
    main_subject_name = None
    main_subject_rate = None
    sub_rates = None

    def __init__(self, id, main_subject_name, main_subject_rate, sub_rates):
        self.id = id
        self.main_subject_name = main_subject_name
        self.main_subject_rate = main_subject_rate
        self.sub_rates = sub_rates


class SubRate:
    id = None
    sub_name = None
    sub_rate = None

    def __init__(self, id, sub_name, sub_rate):
        self.id = id
        self.sub_name = sub_name
        self.sub_rate = sub_rate


class Podcast:
    id = None
    name = None
    desc = None
    main_subject = None
    sub_subjects = None

    def __init__(self, id, name, desc, main_subject, sub_subjects):
        self.id = id
        self.name = name
        self.desc = desc
        self.main_subject = main_subject
        self.sub_subjects = sub_subjects


class SubSubject:
    id = None
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name


from app import mongo


@models.route('/install-db')
def intsall():
    mongo.db.create_collection("Podcasts")
    mongo.db.create_collection("Users")
    return "db initated"
