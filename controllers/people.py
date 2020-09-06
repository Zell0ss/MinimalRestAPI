from flask import make_response, abort
from config import db
from models.person import  Person,  PersonSchema
from models.note import  Note

# Create a handler for our read (GET) people
def read_all():
    """
    GET /api/people
    This function responds to a request for /api/people
    with the complete lists of people

    :return:       the complete sorted list of people
    """
    # query the person database table for all the records (no filter),
    # sort them in ascending order (the default sorting order)
    # Create the list of person objects (people)
    people = (Person.query
            .order_by(Person.lname)
            .all()
    )

    # Serialize the data for the response (marshmallow)
    # many=true => expect an iterable rather than only one record
    person_schema = PersonSchema(many=True)
    data = person_schema.dump(people)
    return data

def read_one(person_id):
    """
    GET /api/people/{person_id}
    This function responds to a request for /api/people/{person_id}
    with one matching person from people and his posts

    :param person_id:   id of person to find
    :return:        person matching last name
    """
    # Get the person requested: query for one or none with the ID passed
    # If none found returns None instead an empty Person
    person = (Person.query
        .filter(Person.person_id == person_id)
        .outerjoin(Note)
        .one_or_none()
    )

    # Does the person exist in people? if yes: serialize (one object so many=False)
    # and return
    if person is not None:
        person_schema = PersonSchema()
        data = person_schema.dump(person)
        return data

    # otherwise, nope, not found
    abort(404, f"Person with ID: {person_id} not found in database")



def create(person):
    """
    This function creates a new person in the people structure
    based on the passed in person data

    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """

    #param parsing
    heroname = person.get("heroname", None)
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person exist already?
    existing_person  = (Person.query
        .filter(Person.heroname == heroname)
        .filter(Person.fname == fname)
        .filter(Person.lname == lname)
        .one_or_none()
        )

    if existing_person is None:
        # Create a person instance using the schema and the passed-in person
        # You use marshmallow to decode and to *encode*
        schema = PersonSchema()
        new_person = schema.load(person, session=db.session)

        # Add the person to the database. ID and UTC timestamp are auto generated
        db.session.add(new_person)
        db.session.commit()

        # Serialize (decode, again) and return the newly created person
        # Creates a 201 specific response instead the normal 200
        # it is unfortunate that abort and make_response have the parameters in different order
        return schema.dump(new_person), 201

    # Otherwise, they exist, that's an error
    else:
        abort(
            406, f"Person {heroname}: {lname}, {fname} already exists",
        )


def update(person_id, person):
    """
    This function updates an existing person in the people structure

    :param heroname:   heroname name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # parse the person
    heroname = person.get("heroname", None)
    lname = person.get("lname", None)
    fname = person.get("fname", None)

    # Does the person to update exists?
    update_person   = Person.query \
        .filter(Person.person_id == person_id) \
        .one_or_none()

    # Are there other person with the same name, surname and heroname?
    existing_person  = Person.query \
        .filter(Person.heroname == heroname) \
        .filter(Person.fname == fname) \
        .filter(Person.lname == lname) \
        .one_or_none()

    # person to update doesnt exists
    if update_person  is None:
        abort(
            404, f"Person with id {person_id} not found"
        )
    # new data to update already exists and its not him
    elif (existing_person is not None and existing_person.person_id != person_id):
        abort(
            404, f"Person data {heroname}: {lname}, {fname} duplicated with id {existing_person.person_id}"
        )
    # otherwise, update away
    else:
        # turn the passed in person into a db object
        schema = PersonSchema()
        update = schema.load(person, session=db.session)

        # Set the id to the person we want to update
        update.person_id = update_person.person_id

        # merge the new object into the old and commit it to the db
        db.session.merge(update)
        db.session.commit()

        # return updated person in the response
        data = schema.dump(update_person)

        return data, 200


def delete(person_id):
    """
    This function deletes a person and his psots from the people structure

    :param person_id:   person_id name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    delete_me = Person.query \
        .filter(Person.person_id == person_id) \
        .one_or_none()
    if delete_me is not None:
        db.session.delete(delete_me)
        db.session.commit()
        return make_response(
            f"Person {person_id} successfully deleted", 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {heroname} not found"
        )
