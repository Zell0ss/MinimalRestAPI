from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Static Data to serve with our API
PEOPLE = {
    "Superman": {
        "fname": "Clark",
        "lname": "Kent",
        "timestamp": get_timestamp()
    },
    "Batman": {
        "fname": "Bruce",
        "lname": "Wayne",
        "timestamp": get_timestamp()
    },
    "Green Lantern": {
        "fname": "Hal",
        "lname": "Jordan",
        "timestamp": get_timestamp()
    },
    "Flash": {
        "fname": "Barry",
        "lname": "Allen",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [PEOPLE[key] for key in sorted(PEOPLE.keys())]
