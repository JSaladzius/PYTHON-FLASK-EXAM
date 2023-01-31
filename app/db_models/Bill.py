from app import db
from flask_authorize import PermissionsMixin
from app.db_models.User import User


class GroupBill(db.Model):
    __tablename__ = "Bills"
    __permissions__ = dict(
        group=['read', 'update'],  
    )
    id = db.Column(db.Integer, primary_key=True)
    discription = db.Column(db.String(255),nullable=False)
    amount = db.Column(db.Integer,nullable=False)
    id_group = db.Column(db.Integer)
    
    def __init__(self, discription , amount, id_group):
        self.discription = discription
        self.amount = amount
        self.id_group = id_group
        