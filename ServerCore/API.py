from flask import Response, request, Blueprint
import json

api = Blueprint('API', __name__, 'ServerCore')

from ServerCore.Models import *
from ServerCore.Core import mongo
from ServerCore.APIResponse import *


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
            sub_subjects.append(SubSubject(i, ss).__dict__)

        podcast = Podcast(body["id"], body["name"], body["desc"], body["main_subject"], sub_subjects)

        res = mongo.db.Podcasts.save(podcast.__dict__)
        return Response(str(res) + " created successfully!")

    elif request.method == "PUT":
        body = request.json

        if mongo.db.Podcasts.find({"id": body["id"]}).count() < 1:
            return "This Podcast doesn't exist!"

        sub_subjects = []
        for i, ss in enumerate(body["sub_subjects"]):
            sub_subjects.append(SubSubject(i, ss).__dict__)

        podcast = Podcast(body["id"], body["name"], body["desc"], body["main_subject"], sub_subjects)

        res = mongo.db.Podcasts.update({"id": body["id"]}, podcast.__dict__)
        return Response(json.dumps(res), mimetype="application/json")

    elif request.method == "DELETE":
        return 1


@api.route('/Podcasts', methods=["GET"])
def get_podcasts():
        res = list(mongo.db.Podcasts.find({}, {'_id': 0}))
        return Response(json.dumps(res), mimetype="application/json")
