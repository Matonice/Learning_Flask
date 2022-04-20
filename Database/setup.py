from app import db, Puppy

## create all the table name
db.create_all()

sam = Puppy('Sammy', 3)
rufus = Puppy('Rufus', 4)

print(sam.id)
print(rufus.id)

#Adding them to the database
db.session.add_all([sam, rufus])

#commiting the changes inside the table
db.session.commit()

print(sam.id)
print(rufus.id)
