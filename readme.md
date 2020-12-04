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

https://casting-agency-test5.herokuapp.com/

###### To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.

OATH login url. There are three logins atm, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.


https://dev-fa25pxj9.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=8g6QGNtR46lknRCWcl70du677jY51SbN&redirect_uri=http://127.0.0.1:5000/

casting Assistant token who has 
"permissions": [
    "view:actors",
    "view:movies"

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyNzY2ODcwMjQ5NDY3MTY1NjQiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDYyODc1LCJleHAiOjE2MDcwNzAwNzUsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.rOQWKS17zc_moBAh0gOHCbKBCdEuZgwq-EQrLrmqJ9uSFfTo8oaxea7_ePuAdnYGYcFz3uXRY5n3gfHyJKSQqUghDQFd9EMH5hHZr4ViYoLuSMbwa65UqnyYPsg1IDfBxiUpNouUJuQQejbtbTlvfVtawrMA-TMWSMsNnOMgOgpT9vaV4MtWLF92GMn6rd-kFl6WuDihlBeETjyu_X6gNIfEyVt-VugeCHETHXy16TXoBpLSMSgoYNzlYST0tjBY2XZTl0qKdtk1oc-yu5_vEUhpHqz2DOwZyCSyfMkaJaVioLqWK6EF7U2bEurmsimLM-TzF-NQmiXbSvAJcCuySg
```

Casting director token who has 
"permissions": [
    "add:actors",
    "delete:actors",
    "patch:actors",
    "patch:movies",
    "view:actors",
    "view:movies"

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNTk1MjgyOTkwNjE3OTY4ODgiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDYyOTUyLCJleHAiOjE2MDcwNzAxNTIsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.UIUmCuGXPHauwd-JMojhAKe1vBTP5AH8-ESboH72GiskvtKIWNv7bxHCYMIQH00MCf9Zr7lo0Zx6OWIvAmef2ld_y-7j6azRcNBZy8R55S2PxnfebxJR4wluq-s4a_GzbZqCHdz36yFsi7TKBB-VZ8Tgryrn2T5f1wv5NRvxIENI2ZqVgXbVgROz4IlKMW4BJ3tOuVulAC1XouQzDMs0pzoz95skBagHfCocbqbkt9LFpn4IZX1aybEXA14ylY5f5R_2T8lqvrfJ4m8uCkySJ2D7wevGCjTiNCwWn2duXEWP27Tp5Jr7Da4RFgKQ6w80J87OeFLaqnrQpRRqBIV-VA
```

Executive Producer who has 
"permissions": [
    "add:actors",
    "add:movies",
    "delete:actors",
    "delete:movies",
    "patch:actors",
    "patch:movies",
    "view:actors",
    "view:movies"

```
eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc2OTE3MjcyMDc3OTcxNTczMTUiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDYzMDMwLCJleHAiOjE2MDcwNzAyMzAsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.oiATkrDeYWlxCl4n0h-oKGRudVrg_TLjxyia7C2gStacFAcqP28SkQzHEbP4WxgqCLv1ia9ylVUh00GOE0pzdAXn-abk6sZGxeWilVeMUhEVq6GX-pK9Gh2lGLGoy9eXJgkQIiB3M5qM4usUNj4FSon9smRg6YM0RnSnNcZFlk-ayvz5Rexh7aQbpO7TdduIIEVhLd2LPtfYTObYhPqKd6Kw5f2rbc99DjaNf2fHKsMyKZRuEgvYLI96lOzqBfHc2dtL9EM74q4IcN-9r0ffBLbE4qjEpqFd3NskCCJZRhMtVQHYd62LAtDxH4KzCfll8Cruj4aHDZP7LnRKrXg-ow```

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
