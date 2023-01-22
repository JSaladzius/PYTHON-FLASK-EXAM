from app import db

class GroupBill(db.Model):
    __tablename__ = "Bills"
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(255),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    what_group = db.relationship('Group' , backref = 'Bills')
    
    def __init__(self, id , discription , amount):
        self.discription = discription
        self.amount = amount
        self.id = id
        