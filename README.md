# Udacity Full Stack Web Development - Capstone Project

## Project

This project has been completed as part of the Udacity Full Stack Web Developer Nanodegree program. The context of this application is a casting agency system that manages actors and movies. Users will roles have different permissions attached such as adding movies and actors, updating, deleting and retrieving. The API is backed by a relational database architecture. The following database tables exist:

- Movie
- Actor
- actor_movies (This is an association table that facilitates the many-to-many relationship between the Actor and Movies tables)

The application is deployed on Heroku - https://casting-agency-brett-123.herokuapp.com

## Tech Stack

Key technologies used

- Python
- Flask framework
- PostgresSQL
- Heroku
- Auth0

## Local environment setup

1. Setup and activate a Python virtual environment. Following steps are using Gitbash CLI

if no python virtul environment previous setup, run this command:

```bash
python -m venv myvenv
```

If there is already a virtual environment created (a folder named myvenv or similiar). Run the following commands to activate the environment:

```bash
cd myvenv/Scripts
. activate
```

2. Install backend dependencies using PIP (Package Installer for Python). This will install the dependencies within the previously activated virtual environment. Packages will now be installed in myvenv/Lib/site-packages

```bash
cd capstone-project
pip install -r requirements.txt
```

## Authentication

The application is authenticated using Auth0. Access token can be generated using the following link:

Token generation - https://casting-agency-brett.eu.auth0.com/authorize?audience=casting-agency&response_type=token&client_id=ROvStzhAFLT1Kxy9SQ86Fq9WTsfbWezV&redirect_uri=http://0.0.0.0:8080

Access tokens must be passed in as an API header on all requests:

```bash
"Authorization": "Bearer {ACCESS-TOKEN}""
```

## Run the application locally

```bash
export FLASK_APP=app.py
flask run --reload
```

## API Endpoints

### GET /actors

Sample request

```bash
curl http://127.0.0.1:5000/actors
```

Sample response

```bash
{
   "actors":[
      {
         "age":"47",
         "gender":"MALE",
         "id":1,
         "movie_id":null,
         "name":"bob"
      },
      {
         "age":"39",
         "gender":"FEMALE",
         "id":2,
         "movie_id":null,
         "name":"barbara"
      }
   ],
   "success":true
}
```

### POST /actors

Sample request

```bash
curl -X POST http://127.0.0.1:5000/actors
   -H 'Content-Type: application/json'
   -d '{
    "name": "Leonardo",
    "age": 54,
    "gender": "MALE",
    "movies": [1,2]
}'
```

Sample response

```bash
{
    "actor": {
        "age": "54",
        "gender": "MALE",
        "id": 3,
        "movies": [
            1,
            2
        ],
        "name": "Leonardo"
    },
    "success": true
}
```

### PATCH /actors/{actor_id}

Sample request

```bash
curl -X PATCH http://127.0.0.1:5000/actors/1 -H 'Content-Type: application/json'
     -H 'Accept: application/json'
     -d '{"movies": [1]}'
```

Sample response

```bash
{
    "actor": {
        "age": "47",
        "gender": "MALE",
        "id": 1,
        "movies": [
            1
        ],
        "name": "bob"
    },
    "success": true
}
```

### DELETE /actors/{actor_id}

Sample request

```bash
curl -X DELETE http://127.0.0.1:5000/actors/2 -H "Accept: application/json"
```

Sample response

```bash
{
    "deleted": 2,
    "success": true
}

```

### GET /movies

Sample request

```bash
curl http://127.0.0.1:5000/movies
```

Sample response

```bash
{
    "movies": [
        {
            "actors": [
                1
            ],
            "id": 1,
            "release_date": "1997",
            "title": "Titanic"
        },
        {
            "actors": [],
            "id": 2,
            "release_date": "1994",
            "title": "Shawshank Redemption"
        }
    ],
    "success": true
}
```

### POST /movies

Sample request

```bash
curl -X POST http://127.0.0.1:5000/movies
   -H 'Content-Type: application/json'
   -d '{
    "title": "Casino Royal",
    "release_date": "2008",
    "actors": [2,1]
}'
```

Sample response

```bash
{
    "movie": {
        "actors": [
            1,
            2
        ],
        "id": 3,
        "release_date": "2008",
        "title": "Casino Royal"
    },
    "success": true
}
```

### PATCH /movies/{movie_id}

Sample request

```bash
curl -X PATCH http://127.0.0.1:5000/movies/2 -H 'Content-Type: application/json'
     -H 'Accept: application/json'
     -d '{"actors": [1]}'
```

Sample response

```bash
{
    "movie": {
        "actors": [
            1
        ],
        "id": 2,
        "release_date": "1994",
        "title": "Shawshank Redemption"
    },
    "success": true
}
```

### DELETE /movies/{movie_id}

Sample request

```bash
curl -X DELETE http://127.0.0.1:5000/movies/2 -H "Accept: application/json"

```

Sample response
```bash
{
    "deleted": 2,
    "success": true
}
```

## Errors

Example errors that can occur during API requests:

### 400 - Bad request

```
{
    "success": False,
    "error": 400,
    "message": "Bad request"
}
```

### 404 - Not found

```
{
    "success": False,
    "error": 404,
    "message": "Not found"
}
```

### 422 - Unprocessable entity
```
{
    "success": False,
    "error": 422,
    "message": "Unprocessable entity"
}
```

### 500 - Internal server error

```
{
    "success": False,
    "error": 500,
    "message": "Internal server error"
}
```

### 403 - Unauthorised

```
{
    "success": False,
    "error": 403,
    "message": "Unauthorised"
}
```


## Local Testing

To run the tests locally, follow these steps:

1. Uncomment line number 19 in app.py. These additional step will create the test database, and relevent tables.

```
# Uncomment this line when running test_app.py
#db_drop_and_create_all_for_local_test()
```
2. Run the following commands in the git bash CLI. 

```bash
. setup
python test_app.py

```





