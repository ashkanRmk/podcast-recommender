from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
# app.config['MONGO_URI'] = "mongodb://localhost:27017/Recommender"
app.config['MONGO_URI'] = "mongodb://ashkan:moonrise1234@ds145573.mlab.com:45573/recommender"
mongo = PyMongo(app)


from Models import models

app.register_blueprint(models)
from API import api

app.register_blueprint(api)


@app.route('/')
def main():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
