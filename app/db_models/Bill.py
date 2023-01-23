from app import db

# user_group = db.Table('user_group', db.metadata,
#     db.Column('group_id', db.Integer, db.ForeignKey('groups.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('all_users.id')))

class GroupBill(db.Model):
    __tablename__ = "Bills"
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(255),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    # groups = db.relationship('Group', backref='GroupBill' )
    user_id = db.Column(db.Integer, db.ForeignKey("all_users.id"))
    user = db.relationship("User")
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    group = db.relationship("Group")

    def __init__(self, id , discription , amount):
        self.discription = discription
        self.amount = amount
        self.id = id
        