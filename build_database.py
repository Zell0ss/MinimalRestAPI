import os
from config import db
#  imports the Person class definition from the models.py module.
from models.person import Person

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Clark",
        "lname": "Kent",
        "heroname": "Superman"
    },
    {
        "fname": "Bruce",
        "lname": "Wayne",
        "heroname": "Batman"
    },
    {
        "fname": "Hal",
        "lname": "Jordan",
        "heroname": "Green Lantern"
    },
    {
        "fname": "Barry",
        "lname": "Allen",
        "heroname": "Flash"
    }
]


# Delete database file if it exists currently
if os.path.exists('people.db'):
    os.remove('people.db')


# Create the database
db.create_all()


# Iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person['lname'], fname=person['fname'], heroname=person['heroname'])
    db.session.add(p)

db.session.commit()
