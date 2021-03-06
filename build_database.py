import os
from datetime import datetime
from config import db
#  imports the Person class definition from the models.py module.
from models.person import Person
from models.note import Note

# Data to initialize database with
PEOPLE = [
    {
        "fname": "Clark",
        "lname": "Kent",
        "heroname": "Superman",
        "notes": [
            ("Cool, a mini-blogging application!", "2019-01-06 22:17:54"),
            ("This could be useful", "2019-01-08 22:17:54"),
            ("Well, sort of useful", "2019-03-06 22:17:54"),
        ],
    },
    {
        "fname": "Bruce",
        "lname": "Wayne",
        "heroname": "Batman",
        "notes": [
            (
                "I'm going to make really profound observations",
                "2019-01-07 22:17:54",
            ),
            (
                "Maybe they'll be more obvious than I thought",
                "2019-02-06 22:17:54",
            ),
        ]
    },
    {
        "fname": "Hal",
        "lname": "Jordan",
        "heroname": "Green Lantern",
        "notes": [
            ("Has anyone seen my Easter eggs?", "2019-01-07 22:47:54"),
            ("I'm really late delivering these!", "2019-04-06 22:17:54"),
        ],
    },
    {
        "fname": "Barry",
        "lname": "Allen",
        "heroname": "Flash",
        "notes": [
            ("flash fact #1", "2019-01-07 22:47:54"),
            ("flash fact #2: my flash fact 1 is lost", "2019-04-06 22:17:54"),
        ],
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

    # iterate over his notes to add them
    for note in person.get("notes"):
        content, timestamp = note
        p.notes.append(
            Note(
                content=content,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )

    db.session.add(p)

db.session.commit()
