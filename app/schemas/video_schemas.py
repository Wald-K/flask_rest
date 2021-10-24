from marshmallow import Schema, fields


class VideoItemRequestSchema(Schema):
    name = fields.Str()
    views = fields.Integer()
    likes = fields.Integer()


class VideoItemResponseSchema(Schema):
    id = fields.Integer()
    name = fields.Str()
    views = fields.Integer()
    likes = fields.Integer()


class VideoListResponseSchema(Schema):
    videos = fields.List(fields.Nested(VideoItemResponseSchema))
