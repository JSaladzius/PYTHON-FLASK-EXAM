from app import db


class Group(db.Model):
    __tablename__ = "groups"
    group_id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(255), nullable=False)