from models import db, Puppy, Owner, Toy

#CREATING TWO puppies
rufus = Puppy('rufus')
fido = Puppy('fido')

db.session.add_all([rufus, fido])
db.session.commit()

#check
print(Puppy.query.all())

rufus = Puppy.query.filter_by(name='rufus').first()

#creating owners
jose = Owner('Jose', rufus.id)

#giving rufus toys
toy1 = Toy('Chew toy', rufus.id)
toy2 = Toy('ball',rufus.id)

db.session.add_all([jose, toy1, toy2])
db.session.commit()

#grabbing rufus after the additions

rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus)

print(rufus.report_toys())
