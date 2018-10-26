from flask import Response, request, Blueprint
import json

api = Blueprint('API', __name__, 'ServerCore')

from Models import *
from app import mongo
from APIResponse import *


@api.route('/check-api', methods=["POST", "GET"])
def check_api():
    return Response(ApiResponse("OK", "Successfull", "Done"), 200, "application/json")


@api.route('/Podcast', methods=["POST", "PUT", "DELETE"])
def podcast_operations():
    if request.method == "POST":
        body = request.json
        body["id"] = mongo.db.Podcasts.find({}).count() + 1

        sub_subjects = []
        for i, ss in enumerate(body["sub_subjects"]):
            sub_subjects.append(SubSubject(i + 1, ss).__dict__)

        podcast = Podcast(body["id"], body["name"], body["desc"], body["main_subject"], sub_subjects)

        res = mongo.db.Podcasts.save(podcast.__dict__)
        return Response(str(res) + " created successfully!")

    elif request.method == "PUT":
        body = request.json

        if mongo.db.Podcasts.find({"id": body["id"]}).count() < 1:
            return "This Podcast doesn't exist!"

        sub_subjects = []
        for i, ss in enumerate(body["sub_subjects"]):
            sub_subjects.append(SubSubject(i + 1, ss).__dict__)

        podcast = Podcast(body["id"], body["name"], body["desc"], body["main_subject"], sub_subjects)

        res = mongo.db.Podcasts.update({"id": body["id"]}, podcast.__dict__)
        return Response(json.dumps(res), mimetype="application/json")

    elif request.method == "DELETE":
        return 1


@api.route('/Podcasts', methods=["GET"])
def get_podcasts():
    res = list(mongo.db.Podcasts.find({}, {'_id': 0}))
    return Response(json.dumps(res), mimetype="application/json")

"""
@:param gender:int
@:param age:int
@:param ratings:array
    @:param mian_subject_name:string
    @:param mian_subject_rate:int
    @:param sub_ratings:array
        @:param name:string
        @:param rate:int
"""
@api.route('/User', methods=["POST"])
def user_operations():
    user_form = request.json
    user_form["id"] = mongo.db.Users.find({}).count() + 1

    ratings = []
    for rate_id, rate in enumerate(user_form["ratings"]):
        sub_rates = []
        for sub_rate_id, sub_rate in enumerate(rate["sub_ratings"]):
            sub_rates.append(SubRate(sub_rate_id + 1, sub_rate["name"], sub_rate["rate"]).__dict__)

        ratings.append(Rate(rate_id + 1, rate["main_subject_name"],
                            rate["main_subject_rate"], sub_rates).__dict__)

    user = User(user_form["id"], user_form["gender"], user_form["age"], ratings)

    res = mongo.db.Users.save(user.__dict__)
    return Response(str(res) + " created successfully!")
