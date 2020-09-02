# MinimalRestAPI
Schematic RESTAPI blueprint
Based on [Python REST APIs With Flask, Connexion, and SQLAlchemy](https://realpython.com/flask-connexion-rest-api/#the-people-rest-api)

## The People REST API

Action 	HTTP Verb 	URL Path 	Description
Create 	POST 	/api/people 	Defines a unique URL to create a new person
Read 	GET 	/api/people 	Defines a unique URL to read a collection of people
Read 	GET 	/api/people/Farrell 	Defines a unique URL to read a particular person in the people collection
Update 	PUT 	/api/people/Farrell 	Defines a unique URL to update an existing order
Delete 	DELETE 	/api/orders/Farrell 	Defines a unique URL to delete an existing person

## swagger in localhost:5000/mrapi/ui