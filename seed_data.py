from app import db
from app.db_models.Bill import GroupBill
from app.db_models.Group import Group

db.create_all()

bill1 = GroupBill('1', 'Ledai', '6' )
bill2 = GroupBill('2', 'Vėliavėlės', '7' )
bill3 = GroupBill('3', 'Kinobilietai', '20' )

db.session.add_all([bill1, bill2, bill3])
db.session.commit()

group1 = Group('1', 'Gedo Bokstas')
group2 = Group('2', 'Ispanija')
group3 = Group('3', 'Kino Pavasaris')
group4 = Group('4', 'Iskyla i pelkes')

db.session.add_all([group1, group2, group3, group4])
db.session.commit()




