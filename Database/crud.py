from app import db, Puppy

##create
my_puppy = Puppy('Frankie', 5)
db.session.add(my_puppy)
db.session.commit()

#READ
all_puppies = Puppy.query.all()
print(all_puppies)

#Select by
puppy_one = Puppy.query.get(1)
print(puppy_one.name)

#filter
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())

##update
first_puppy = Puppy.query.get(1)
first_puppy.age=10
db.session.add(first_puppy)
db.session.commit()

#delete
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

#
all_puppies = Puppy.query.all()
print(all_puppies)
