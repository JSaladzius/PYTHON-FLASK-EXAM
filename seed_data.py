from app import db
from app.db_models.Bill import GroupBill
from app.db_models.Group import Group , user_group
from app.db_models.User import User


db.create_all()

user1 = User('Jonas', '	jonas@jonas.lt','jonas123' )
user2 = User('Petras', 'petras@petras.lt','petras123' )
user3 = User( 'Domas', 'domas@domas.lt','$2b$12$H3iGqTZJC9x3JS8q8jD1kerzbOUNJjNrYIrDkoQ.7lmFvs8hcq2Ja' )
user4 = User('Kazys', 'kazys@kazys.lt','kazys123' )

db.session.add_all([user1, user2, user3, user4])
db.session.commit()

group1 = Group('1', 'Gedo Bokstas')
group2 = Group('2', 'Ispanija')
group3 = Group('3', 'Kino Pavasaris')
group4 = Group('4', 'Iskyla i pelkes')

group1.users.append(user1)
group1.users.append(user2)

group2.users.append(user1)
group2.users.append(user3)
group2.users.append(user4)

group3.users.append(user2)
group3.users.append(user4)

group4.users.append(user1)
group4.users.append(user2)
group4.users.append(user3)
group4.users.append(user4)


db.session.add_all([group1, group2, group3, group4])
db.session.commit()


bill1 = GroupBill( 'Ledai', '6', '1' )
bill2 = GroupBill( 'Vėliavėlės', '7','1' )
bill3 = GroupBill( 'Kinobilietai', '20' , '3')
bill4 = GroupBill( 'Kalnas alyvuogiu', '30' , '2')

db.session.add_all([bill1, bill2, bill3])
db.session.commit()

