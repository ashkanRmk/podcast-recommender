import json

class ApiResponse:
    d = dict()

    def __init__(self, status=None, message=None, result=None):
        self.d["status"] = status
        self.d["msg"] = message
        self.d["res"] = result

    def to_json(self):
        return json.dumps(self.d)
