from app import db


class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __init__(self, name, views, likes):
        self.name = name
        self.views = views
        self.likes = likes

    def __repr__(self) -> str:
        return f"Video(id={self.id}, name={self.name}, \
            views={self.views}, likes={self.likes})"
