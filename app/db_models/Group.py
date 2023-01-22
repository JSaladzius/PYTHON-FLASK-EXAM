from app import db

user_group = db.Table('user_group', db.metadata,
    db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
    db.Column('user_id', db.Integer, db.ForeignKey('all_users.id'))
)

class Group(db.Model):
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True)
    trip_name = db.Column(db.String(255), nullable=False)
    bill_id = db.Column(db.Integer, db.ForeignKey('Bills.id'))

    users = db.relationship('User', secondary=user_group, backref='groups')


    def __init__(self, id, trip_name):
        self.id = id
        self.trip_name = trip_name


        