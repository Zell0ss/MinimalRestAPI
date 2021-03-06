# MinimalRestAPI
Schematic RESTAPI blueprint
Based on [Python REST APIs With Flask, Connexion, and SQLAlchemy](https://realpython.com/flask-connexion-rest-api/#the-people-rest-api)

## The People REST API

Action 	HTTP Verb 	URL Path 	Description
- Create 	POST 	/mrapi/people 	Defines a unique URL to create a new person
- Read 	GET 	/mrapi/people 	Defines a unique URL to read a collection of people
- Read 	GET 	/mrapi/people/{person_id} 	Defines a unique URL to read a particular person in the people collection
- Update 	PUT 	/mrapi/people/{person_id} 	Defines a unique URL to update an existing order
- Delete 	DELETE 	/mrapi/orders/{person_id} 	Defines a unique URL to delete an existing person

- Create 	POST 	/mrapi/people/{person_id}/notes 	URL to create a new note
- Read 	GET 	/mrapi/people/{person_id}/notes/{note_id} 	URL to read a single person’s single note
- Read 	GET 	/mrapi/people/{person_id}/notes 	URL to read a single person’s all notes
- Update 	PUT 	mrapi/people/{person_id}/notes/{note_id} 	URL to update a single person’s single note
- Delete 	DELETE 	mrapi/people/{person_id}/notes/{note_id} 	URL to delete a single person’s single note
- Read 	GET 	/mrapi/notes 	URL to get all notes for all people sorted by note.timestamp


## swagger 
Generated by connexion and created with swagger.yml.

UI in http://localhost:5000/mrapi/ui

## connexion & Marshmallow


# linting in VSCODE

## flask
Using pylint with either:

```
"python.linting.pylintArgs": ["--load-plugins", "pylint-flask"]
"python.linting.pylintArgs": ["--load-plugins", "pylint_flask"]
```

## modules
Add to .pylintrc 

```
[MASTER]
init-hook='import sys; sys.path.append("/path/to/root")'
```