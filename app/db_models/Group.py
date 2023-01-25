from app import db
from flask_authorize import RestrictionsMixin


user_group = db.Table('user_group', db.metadata,
    db.Column('id', db.Integer , primary_key=True),
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('all_users.id'))
)

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(255), nullable=False)
    users = db.relationship('User',secondary=user_group)
    # , backref='group'
    
    def __init__(self, id, trip_name):
        self.id = id
        self.trip_name = trip_name


        