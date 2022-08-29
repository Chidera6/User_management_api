API Documentation

This repository contains only the backend for this app.
This is a User management App,this app attempts to get the database of everyone worldwide, It stores all the countries in its database while users registers base on their countries.Users can also activate or deactivate their profiles using this app.

Getting Started
Pre-requisites and Local Development
Developers using this project should already have Python3, pip and node installed on their local machines.

Backend
From the backend folder run pip install -r requirements.txt. All required packages are included in the requirements file.

To run the application run the following commands:
export FLASK_APP=user_app
export FLASK_ENV=development
flask run
These commands put the application in development and directs our application to use the app.py file in our user_app folder. Working in development mode shows an interactive debugger in the console and restarts the server whenever changes are made. If running locally on Windows, the command python -m flask run will make the application run in development.

The application is run on http://127.0.0.1:5000/ by default.All tests are kept in test.py file and should be maintained as updates are made to app functionality.

API Reference
Endpoints

GET '/countries'
- An external API that gets all countries and stores them in the database.


GET '/countries'
- Fetches a list of countries in the database.
- Request Arguments: None
- Returns: 
Sample: curl http://127.0.0.1:5000/countries

GET '/users'
- Fetches all the users in the app.
- Request Arguments: None
- Returns: 
Sample: curl http://127.0.0.1:5000/users

PATCH '/users/<int:user_id>>'
- updates  users by id..
Sample: curl http://127.0.0.1:5000/users/3


GET '/activate/<int:user_id>'
- Fetches all the users in the app by id.
then you can activate the user.
Sample: curl http://127.0.0.1:5000/users/5

GET '/deactivate/<int:user_id>'
- Fetches all the users in the app by id.
then you can activate the user.
Sample: curl http://127.0.0.1:5000/users/5

GET '/users/<int:user_id>'
- Fetches users by their id. 
- Request Arguments: id - integer
Sample: curl http://127.0.0.1:5000/users/5

DELETE '/users/<int:user_id>'
- Deletes a specified question using the id of the question
- Request Arguments: id - integer 
Sample curl -X DELETE http://127.0.0.1:5000/users/2

POST '/create'
- Sends a post request in other to create a user. 
Sample curl http://127.0.0.1:5000/create -X POST -H "Content-Type: application/json" -d '{"country_name":"Nigeria","first_name":"chidera", "last_name":"stella", "email":"dictasteil@gmail.com", "phone":"2349166"}'


