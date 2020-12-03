# Full Stack Casting Agency API Backend

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

This is the capstone project of Udacity fullstack nanodegree program, which demonstrate the skillset of using Flask, SQLAlchemy, Auth0, gunicorn and heroku to develop and deploy a RESTful API. 

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql casting_agency<casting_agency.psql
```

more info here:
https://www.linode.com/docs/databases/postgresql/how-to-back-up-your-postgresql-database/#:~:text=PostgreSQL%20provides%20the%20pg_dump%20utility,you%20intend%20to%20back%20up.&text=Dump%20the%20contents%20of%20a,database%20to%20be%20backed%20up.

## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
. ./setup.sh
flask run
```

#### Flask run tests the token headers set for the enviroment. If they have expired, you need to login using the crededntials below and replace them in setup.sh and run setup.sh again

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

# Project deployed at

https://fsnd-casting-agency-udacity.herokuapp.com/

###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

OATH login url. There are three logins atm, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.


https://dev-fa25pxj9.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=8g6QGNtR46lknRCWcl70du677jY51SbN&redirect_uri=http://127.0.0.1:5000/

casting Assistant token 

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyNzY2ODcwMjQ5NDY3MTY1NjQiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDMwMDM5LCJleHAiOjE2MDcwMzcyMzksImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.6W9TS3XYbl6zey3oeGkVk9f24BH5kCvUu6jX1SdZtCM5uQ0Y7mZQ4mgxwU8hpqPC5-H05O2705-V2FyRbZF7F9wm6IyKTXsppBlmURLHLFNDT95iJkKyxZdWlXlAMhdQRYllXF-zFx9fi300JI7PzxQp_IOzA5lnNFgpVM1MeInpCMr1kDyCXKSYojZcaeBHm5G7I2852-cdapKQ8Ulh_mAHRIXkaEOs14y61dDBkvfSndCNrC43-a3iZblkeNOjL_eKD1445NA1BI7sqUVVGHFkefuvbyE8hPt2b4KwlOja8q7AItNI81Gps7tOVoW-p8Jiw1fpX8iVgrY-TMlcTw
```

Casting director token 

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNTk1MjgyOTkwNjE3OTY4ODgiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDI5OTMzLCJleHAiOjE2MDcwMzcxMzMsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.N5kO_tnxtGOLdQQxxXdxPMJMhB_V7EAfgKSzl9wxWDpJXB1e2pi0-8VxxgHDMbBB4MN4FY1Ozko07HvIP6R_D6ydBDh57Qg5DTFzJbwTA5eSGYXONFSKR4zPisACpz88xCEMqf1s_hb4dWDq6G0UK4RUbPg52NEmKsgNYI-SVOkIU2L4GQwO_WiksPUox04bMUXi51WrZlPjE-kSzk8_u1lz4J7qZBYIivEsGozjAsIDjpdiBq6zwJMSzQPsvGsnXKWQdY52j6uYsnRuArgMKgT2gAGGy5DfCUWDCEA8rQR16xQuiuOHwLaEqGjsUnBeD08QCmQv9rRddN4qDGB0mw
```

Executive Producer 

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc2OTE3MjcyMDc3OTcxNTczMTUiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDMwMTM0LCJleHAiOjE2MDcwMzczMzQsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.VI1kKwI5EWMnCw6JTUHFxcvjFa8LuNKiNvY5fRT42U9Jo7trfYKjfw4VZbFlfIApjSWnsKwR0OgnrZMhD0DO5_8PV9woRwGpy5MuTVwXy0QK-ugD-nZVtTrDWyByZrgX9gDNQ7XVWUWGOn1frBGRU8mMYU6ZfXNk3KQTc5-iIWbdGaTr64QY32hAHBY-ePjnCnox0Xheg6WTSOORPflDJD1tvpnAR4ftJQS-XsYvbVJN-k-jAmVk4TSnotWgDRuJYREwuLcZTVqA8YoRSQ9zn0vSEj_Rv2vidcpOLE1piLXA1FnygaH68QKyXBU8m8eQPOLmRBn-vueA5p4gYsA0Nw```

## Testing

To run the tests, run

```
dropdb casting_agency_test
createdb casting_agency_test
psql casting_agency_test<casting_agency_test.psql
python test_flaskr.py
```

The tests print data returned from the APIs along with API logs.

#### The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 400,
    "message": "bad request"
}

```

### Endpoints

GET '/actors'
POST '/actors'
PATCH '/actors/<actor_id>'
DELETE '/actors/<actor_id>'
GET '/movies'
POST '/movies'
PATCH '/movies/<movie_id>'
DELETE '/movies/<movie_id>'

GET '/movies'
Fetches an array of movies
Required URL Arguments: None
Required Data Arguments: None
Returns: Returns Json data about movies
Success Response:

```
{
    "movies": [
        {
            "genre": "SuperHero",
            "id": 1,
            "release_date": "2019-01-02",
            "title": "Spider-Man"
        },
        {
            "genre": "romantic",
            "id": 4,
            "release_date": "2020-01-02",
            "title": "The Perfect Date"
        }
    ],
    "success": true
}
```

GET '/actors'
Fetches an array of actors
Required Data Arguments: None
Returns: Json data about actors
Success Response:

```
  {
    "actors": [
        {
            "age": 21,
            "gender": "male",
            "id": 1,
            "name": "ahmed"
        },
        {
            "age": 21,
            "gender": "male",
            "id": 2,
            "name": "sayed"
        },
        {
            "age": 21,
            "gender": "male",
            "id": 4,
            "name": "ahmed helmy"
        },
        {
            "age": 70,
            "gender": "female",
            "id": 6,
            "name": "mona zaki"
        },
        {
            "age": 21,
            "gender": "male",
            "id": 7,
            "name": "ahmed"
        }
    ],
    "success": true
}
```

DELETE '/movies/<int:movie_id>'
Deletes the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: deleted movie's ID and name
Success Response:

```
{
    "deleted": 1,
    "name": "Spider-Man",
    "success": true
}
```

DELETE '/actors/<int:actor_id>'
Deletes the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns:the deleted actor's ID and name
Success Response:

```
{
    "deleted": 7,
    "name": "ahmed",
    "success": true
}
```

POST '/movies'
Post a new movie in a database.
Required URL Arguments: None
Required Data Arguments: Json data
Success Response:

```
{
    "movie_id": 5,
    "success": true
}
```

POST '/actors'
Post a new actor in a database.

Required URL Arguments: None

Required Data Arguments: Json data

Success Response:

```
{
    "actor_id": 8,
    "success": true
}
```

PATCH '/movies/<int:movie_id>'
Updates the movie_id of movie
Required URL Arguments: movie_id: movie_id_integer
Required Data Arguments: None
Returns: Json data about the updated movie
Success Response:

```
{
    "movie": {
        "genre": "SuperHero",
        "id": 5,
        "release_date": "2019-01-02",
        "title": "Avengers 2"
    },
    "success": true
}
```

PATCH '/actors/<int:actor_id>'
Updates the actor_id of actor
Required URL Arguments: actor_id: actor_id_integer
Required Data Arguments: None
Returns: Json data about the modified actor's ID
Success Response:

```
{
   "actor":{
      "age":22,
      "gender":"male",
      "id":10,
      "name":"gopi"
   },
   "success":True
}
```

## Authors

Rishabh Gajra and The udacity team that made the starter code and Project tasks.
