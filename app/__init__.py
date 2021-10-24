from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///./test.db"

db = SQLAlchemy(app)
from app.resources.video_resources import VideoItemResource, VideoResource

api = Api(app)


api.add_resource(VideoResource, "/video")
api.add_resource(VideoItemResource, "/video/<int:video_id>")
