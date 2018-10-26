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
        data = request.json
        if mongo.db.Podcasts.find({"id": data["id"]}).count() > 0:
            return "id alreay exists"
        subsets = []
        for ss in data["subsets"]:
            subsets.append(Subset(ss["id"], ss["name"]).__dict__)
        podcast = Podcast(data["id"], data["name"], data["desc"], data["main"], subsets)
        res = mongo.db.Podcasts.save(podcast.__dict__)
        return Response(str(res) + " created")
    elif request.method == "PUT":
        data = request.json
        subsets = []
        for ss in data["subsets"]:
            subsets.append(Subset(ss["id"], ss["name"]).__dict__)
        podcast = Podcast(data["id"], data["name"], data["desc"], data["main"], subsets)
        res = mongo.db.Podcasts.update({"id": data["id"]}, podcast.__dict__)
        return Response(json.dumps(res), mimetype="application/json")
    elif request.method == "DELETE":
        return pass


@api.route('/Podcasts', methods=["GET"])
def get_podcasts():
        res = list(mongo.db.Podcasts.find({}, {'_id': 0}))
        return Response(json.dumps(res), mimetype="application/json")