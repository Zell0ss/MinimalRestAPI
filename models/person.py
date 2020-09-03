from datetime import datetime
#get the database and marsmallow apps
from sqlalchemy import true
from config import db, ma

class Person(db.Model):
    __tablename__ = 'person'
    person_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32))
    fname = db.Column(db.String(32))
    heroname = db.Column(db.String(32), index=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        sqla_session = db.session
        load_instance = true
