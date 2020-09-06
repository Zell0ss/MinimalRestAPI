from datetime import datetime
#get the database and marsmallow apps
from sqlalchemy import true
from config import db, ma
# this I need for the relationship but as Note is passed as a string rather than an objet
# the lynter doesnt know its used and complains
from models.note import Note # pylint: disable=unused-import

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    heroname = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    notes = db.relationship(
        'Note',
        # backwards reference in Note objects.
        # Each instance of a Note object will contain an attribute called person.
        # The person attribute references the parent object that a particular Note instance is associated with
        backref='person',
        # cascade deletion
        cascade='all, delete, delete-orphan',
        single_parent=True,
        order_by='desc(Note.timestamp)'
    )


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session
        load_instance = true
