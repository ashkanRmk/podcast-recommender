from flask import Flask, blueprints, Response
from ServerCore.Models import models, db
from ServerCore.API import api

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mirhajian' \
                                        '@localhost:5432/RecommenderDB'

app.register_blueprint(models)
app.register_blueprint(api)
db.init_app(app)


@app.route('/')
def main():
    return "OK"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
