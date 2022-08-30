API Documentation

This repository contains only the backend for this app.
This is a User management App,this app attempts to get the database of everyone worldwide, It stores all the countries in its database while users registers base on their countries.Users can also activate or deactivate their profiles using this app.

Getting Started

Pre-requisites and Local Development
Developers using this project should already have Python3 and pip installed on their local machines.

Backend
From the user_management folder run pip install -r requirements.txt. All required packages are included in the requirements file.

To run the application run the following commands:
export FLASK_APP=user_app
export FLASK_ENV=development
flask run
These commands put the application in development and directs our application to use the __init__.py file in our flaskr folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, the command python -m flask run will make the application.

The application is run on http://127.0.0.1:5000/ by default.

API Reference
Endpoints

GET '/countries'
- An external API that gets all countries and stores them in the country database.
This API is strictly for populating the database and it being commented out after the first run.


GET '/countries'
- Fetches a list of countries in the database,paginated.
- Request Arguments: None
- Returns: 
Sample: curl http://127.0.0.1:5000/countries

GET '/users'
- Fetches all the users in the app,paginated.
- Request Arguments: None
- Returns: 
Sample: curl http://127.0.0.1:5000/users

PATCH '/users/<int:user_id>>'
- updates  users by id.
Sample: curl -X PATCH http://127.0.0.1:5000/users/3


GET '/activate/<int:user_id>'
- Fetches a user by id.
then you can activate the user.
Sample: curl -X PATCH http://127.0.0.1:5000/users/5

GET '/deactivate/<int:user_id>'
- Fetches a user by id.
then you can activate the user.
Sample: curl -X PATCH http://127.0.0.1:5000/users/5

GET '/users/<int:user_id>'
- Fetches a user by their id. 
- Request Arguments: id - integer
Sample: curl http://127.0.0.1:5000/users/5

DELETE '/users/<int:user_id>'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer 
Sample curl -X DELETE http://127.0.0.1:5000/users/2

POST '/create'
- Sends a post request in other to create a user. 
Sample curl http://127.0.0.1:5000/create -X POST -H "Content-Type: application/json" -d '{"country_name":"Nigeria","first_name":"chidera", "last_name":"stella", "email":"dictasteil@gmail.com", "phone":2349166,"sex":"female"}'


You can also use postman or thunderclients to test all endpoints.