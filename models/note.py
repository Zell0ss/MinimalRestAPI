from datetime import datetime
#get the database and marsmallow apps
from sqlalchemy import true
from config import db, ma
from marshmallow import fields


class Note(db.Model):
    __tablename__ = 'note'
    note_id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow )

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        sqla_session = db.session
        load_instance = true
    person = fields.Nested('NotePersonSchema', default=None) # could not refer directly to PersonSchema

class NotePersonSchema(ma.SQLAlchemyAutoSchema):
    """
    This class exists to get around a recursion issue
    """
    person_id = fields.Int()
    lname = fields.Str()
    fname = fields.Str()
    heroname = fields.Str()
    timestamp = fields.Str()
