from flask import Response
from ServerCore.Models import *
from ServerCore.APIResponse import *

api = Blueprint('API', __name__, 'ServerCore')


@api.route('/check-api', methods=["POST", "GET"])
def check_api():
    return Response(ApiResponse("OK", "Successfull", "Done"), 200, "application/json")
