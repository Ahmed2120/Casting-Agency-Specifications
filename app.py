from flask import Flask, request, jsonify, abort
from models import setup_db, Actor, Movie, create_and_drop_all, setup_migrations
from flask_cors import CORS
import sys
import datetime
from werkzeug.exceptions import HTTPException, NotFound, PreconditionFailed
from auth import requires_auth, AuthError

def create_app(test_config=None):
    app = Flask(__name__)
    setup_db(app)
    setup_migrations(app)
    # cors headers allow
    CORS(app)
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             "Content-Tpe,Authorization,true")
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,PATCH,DELETE,OPTIONS')
        return response

    create_and_drop_all()
    # routes
    ''' sample route '''
    @app.route('/')
    def index():
        log = """
<div >
<span style='position: absolute;
        border-style: solid,;
        padding: 12;
        text-decoration: none;
        background: cornflowerblue;
        margin-top: 51px;'>
<a  href=
'https://dev-fa25pxj9.us.auth0.com/authorize?audience=
capstone&response_type=
token&client_id=8g6QGNtR46lknRCWcl70du677jY51SbN&redirect_uri
=http://127.0.0.1:5000/' 
style='color: white;
    text-decoration: none;
    font-size: 32px;'>Login
</a>
</span>
</div>"""
        return "Hello world! " + log


    # routes for movies
    @app.route('/movies')
    @requires_auth('view:movies')
    def view_movies(jwt):
        try:
            movies = Movie.query.all()
            if len(movies) == 0:
                abort(404)
            movies = [movie.get_format() for movie in movies]
            return jsonify({"success": True,
                            "movies": movies})
        except :
            return "something wrong"

    @app.route('/movies', methods=['POST'])
    @requires_auth('add:movies')
    def Add_movie(jwt):
        try:
            films = request.get_json()
            if 'title' not in films or 'release_date' not in films or 'genre' not in films:
                abort(400)
            movie = Movie(title=films['title'],
                          release_date=datetime.date.fromisoformat(films['release_date']),
                           genre=films['genre'])
            movie.insert()
            return jsonify({
                "success": True,
                "movie_id": movie.id
            })
        except :
            return "something wrong"

    @app.route('/movies/<int:movie_id>', methods=['PATCH'])
    @requires_auth('patch:movies')
    def Edit_movie(jwt, movie_id):
        try:
            films = request.get_json()
            if films is None:
                abort(400)
            movie = Movie.query.get(movie_id)
            if movie is None:
                abort(404)
            if 'title' in films:
                movie.title = films["title"]
            if 'release_date' in films:
                movie.release_date = films["release_date"]
            if 'genre' in films:
                movie.genre = films["genre"]
            movie.update()
            return jsonify({
                "success": True,
                "movie": movie.get_format()
            })
        except :
            return "something wrong"

    @app.route('/movies/<int:movie_id>', methods=['DELETE'])
    @requires_auth('delete:movies')
    def delete_movie(jwt, movie_id):
        try:
            movie = Movie.query.get(movie_id)
            if movie is None:
                abort(404)
            movie.delete()
            return jsonify({
                "success": True,
                "deleted": movie.id,
                "name": movie.title
            })
        except :
            return "something wrong"

    # routes for actors
    @app.route('/actors')
    @requires_auth('view:actors')
    def view_actors(jwt):
        try:
            actors = Actor.query.all()
            if len(actors) == 0:
                abort(404)
            actors = [actor.get_format() for actor in actors]
            return jsonify({
                "success": True,
                "actors": actors
            })
        except :
            return "something wrong"

    @app.route('/actors', methods=['POST'])
    @requires_auth('add:actors')
    def Add_actor(jwt):
        print("Post api on /actors hit:\n\n")
        try:
            films = request.get_json()
            if 'name' not in films or 'age' not in films or 'gender' not in films:
                abort(400)
            actor = Actor(name=films['name'],
                          age=films['age'], gender=films['gender'])
            actor.insert()
            return jsonify({
                "success": True,
                "actor_id": actor.id
            })
        except :
            return "something wrong"

    @app.route('/actors/<int:actor_id>', methods=['PATCH'])
    @requires_auth('patch:actors')
    def Edit_actor(jwt, actor_id):
        try:
            films = request.get_json()
            if films is None:
                abort(400)
            actor = Actor.query.get(actor_id)
            if actor is None:
                abort(404)
            if 'name' in films:
                actor.name = films["name"]
            if 'age' in films:
                actor.age = films["age"]
            if 'gender' in films:
                actor.gender = films["gender"]
            actor.update()
            return jsonify({
                "success": True,
                "actor": actor.get_format()
            })
        except :
            return "something wrong"

    @app.route('/actors/<int:actor_id>', methods=['DELETE'])
    @requires_auth('delete:actors')
    def delete_actor(jwt, actor_id):
        try:
            actor = Actor.query.get(actor_id)
            if actor is None:
                abort(404)
            actor.delete()
            return jsonify({
                "success": True,
                "deleted": actor.id,
                "name": actor.name
            })
        except :
            return "something wrong"

        # error handlers :

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(412)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 412,
            "message": "Precondition for resouce failed",
            "question": False
        }), 412

    @app.errorhandler(404)
    def error_resource_not_found(error):
        return jsonify({
            "success": False,
            "message": "Resource not found",
            "error": 404
        }), 404

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "message": "Internal server error",
            "error": 500
        }), 500

    @app.errorhandler(422)
    def not_processable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request cant be processed"
        }), 422

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(401)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "Not Authorized"
        })

    @app.errorhandler(403)
    def auth_error(error):
        return jsonify({
            "success": False,
            "error": 403,
            "message": "Forbidden"
        }), 403

    @app.errorhandler(AuthError)
    def auth_error(error):
        print(error)
        return jsonify({
            "success": False,
            "error": error.status_code,
            "message": error.error
        }), error.status_code

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

