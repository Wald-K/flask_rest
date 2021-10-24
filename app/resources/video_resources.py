from flask import abort
from flask.globals import request
from flask_restful import Resource

from app import db
from app.models.video import Video
from app.schemas.video_schemas import (
    VideoItemRequestSchema,
    VideoItemResponseSchema,
    VideoListResponseSchema,
)


def about_if_video_not_exist(video_id, video_library):
    if video_id not in video_library:
        abort(404, message="Video doesnt exist")


def about_if_video_exist(video_id, video_library):
    if video_id in video_library:
        abort(409, message="Video with this Id exists in library")


class VideoResource(Resource):
    def post(self):
        schema = VideoItemRequestSchema()
        data = schema.load(request.form)
        obj = Video(**data)
        db.session.add(obj)
        db.session.commit()
        return {"message": f"object id={obj.id} was created"}, 201

    def get(self):
        # schema = VideoItemResponseSchema(many=True)
        schema = VideoListResponseSchema(many=True)
        data = db.session.query(Video).all()
        result = schema.dump(data)
        print(result)


class VideoItemResource(Resource):
    def get(self, video_id):
        # about_if_video_not_exist(video_id, videos)
        schema = VideoItemResponseSchema()
        obj = db.session.query(Video).filter_by(id=video_id).first()
        if obj is None:
            return {"message": f"object id={video_id} not found"}, 404
        result = schema.dump(obj)
        print(result)
        print(type(result))
        return result

    def delete(self, video_id):
        obj = db.session.query(Video).filter_by(id=video_id).first()
        if obj:
            db.session.query(Video).filter_by(id=video_id).delete()
            db.session.commit()
            return {"message": f"object id={obj.id} was deleted"}, 200
        else:
            return {"message": "object id={video_id} not found"}, 404

    def put(self, video_id):
        obj = db.session.query(Video).filter_by(id=video_id).first()
        if obj is None:
            return {"message": f"object id={video_id} not found"}, 404

        schema = VideoItemRequestSchema()
        data = schema.load(request.form)
        if obj:
            db.session.query(Video).filter_by(id=video_id).update(data)
            db.session.commit()
            return {"message": f"object id={obj.id} was updated"}, 200
        else:
            return {"message": "object id={video_id} not found"}, 404
