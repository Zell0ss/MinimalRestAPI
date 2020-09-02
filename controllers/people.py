# System modules
from datetime import datetime

# 3rd party modules
from flask import make_response, abort

def get_timestamp():
    """
    get current timestamp in UTC
    """
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Create a handler for our read (GET) people
def read_all():
    """
    GET /api/people
    This function responds to a request for /api/people
    with the complete lists of people

    :return:       the complete sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]

def read_one(heroname):
    """
    GET /api/people/{heroname}
    This function responds to a request for /api/people/{heroname}
    with one matching person from people

    :param lname:   last name of person to find
    :return:        person matching last name
    """
    # Does the person exist in people?
    if heroname in PEOPLE:
        person = PEOPLE.get(heroname)

    # otherwise, nope, not found
    else:
        abort(
            404, f"Superheroe {heroname} not found in database"
        )

    return person


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
    if heroname not in PEOPLE and heroname is not None:
        PEOPLE[heroname] = {
            "lname": lname,
            "fname": fname,
            "timestamp": get_timestamp(),
        }
        # Creates a 201 specific response instead the normal 200
        # it is unfortunate that abort and make_response have the parameters in different order
        return make_response(
            f"{heroname} successfully created", 201
        )

    # Otherwise, they exist, that's an error
    else:
        abort(
            406, f"Person with last name {heroname} already exists",
        )


def update(heroname, person):
    """
    This function updates an existing person in the people structure

    :param heroname:   heroname name of person to update in the people structure
    :param person:  person to update
    :return:        updated person structure
    """
    # Does the person exist in people?
    if heroname in PEOPLE:
        PEOPLE[heroname]["fname"] = person.get("fname")
        PEOPLE[heroname]["timestamp"] = get_timestamp()

        return PEOPLE[heroname]

    # otherwise, nope, that's an error
    else:
        abort(
            404, f"Person with last name {heroname} not found"
        )


def delete(heroname):
    """
    This function deletes a person from the people structure

    :param heroname:   heroname name of person to delete
    :return:        200 on successful delete, 404 if not found
    """
    # Does the person to delete exist?
    if heroname in PEOPLE:
        del PEOPLE[heroname]
        return make_response(
            f"{heroname} successfully deleted", 200
        )

    # Otherwise, nope, person to delete not found
    else:
        abort(
            404, "Person with last name {heroname} not found"
        )