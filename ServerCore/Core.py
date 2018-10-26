from flask import Flask, blueprints, Response
from flask_pymongo import PyMongo
from ServerCore.Models import models
from ServerCore.API import api

app = Flask(__name__)
app.config['MONGO_URI'] = "mongodb://localhost:27017/Recommender"
mongo = PyMongo(app, config_prefix='MONGO')
app.register_blueprint(models)
app.register_blueprint(api)


@app.route('/')
def main():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
