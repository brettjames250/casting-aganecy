import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import Actor, Movie, setup_db, db_drop_and_create_all
from auth import requires_auth

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#



# create and configure the app
app = Flask(__name__)
setup_db(app)
CORS(app)
# only uncomment for local testing
#db_drop_and_create_all()
  

API_AUDIENCE = os.environ.get('API_AUDIENCE')
AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
AUTH0_CLIENT_ID = os.environ.get('AUTH0_CLIENT_ID')
AUTH0_CALLBACK_URL = os.environ.get('AUTH0_CALLBACK_URL')

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
  return response

##ACTORS

#GET /actors
@app.route("/actors", methods=["GET"])
def get_actors():
  actors = Actor.query.all()
  
  formatted_actors = []
  for actor in actors:
    formatted_actors.append(actor.format())
    
  return jsonify({
    "success": True,
    "actors": formatted_actors
  })
  
#DELETE /actors/{id}
@app.route("/actors/<int:actor_id>", methods=["DELETE"])
@requires_auth('delete: actors')
def delete_actor(payload, actor_id):
  actor = Actor.query.get(actor_id)
  
  if actor is None:
    abort(404)
  
  actor.delete()
  
  return jsonify({
    "success": True,
    "deleted": actor.id
  })
  
  
#POST /actors
@app.route("/actors", methods=["POST"])
@requires_auth('post: actors')
def add_actor(payload):
  request_data = request.get_json()
  
  name = request_data.get("name"),
  age = request_data.get("age"),
  gender = request_data.get("gender"),
  movie_ids = request_data.get("movies", [])
  
  casted_movies = []
  
  for movie_id in movie_ids:
    movie = Movie.query.get(movie_id)
    if movie is None:
      abort(404)
    else:
      casted_movies.append(movie)
    
    
  new_actor = Actor(
    name=name,
    age=age,
    gender=gender,
    movies = casted_movies
  )
  
  new_actor.insert()
  
  return jsonify({
    "success": True,
    "actor": new_actor.format() 
  })
  
#PATCH /actors/{id}
@app.route("/actors/<int:actor_id>", methods=["PATCH"])
@requires_auth('patch: actors')
def update_actor(payload, actor_id):
  actor = Actor.query.get(actor_id)
  
  if not actor:
    abort(404)
    
  name = request.get_json().get("name", actor.name)
  age = request.get_json().get("age", actor.age)
  gender = request.get_json().get("gender", actor.gender)
  movies = request.get_json().get("movies", [])
  
  if movies is not None:
    formatted_movies = Movie.query.filter(Movie.id.in_(movies)).all()
  else:
    formatted_movies = actor.movies
    
  actor.name = name
  actor.age = age
  actor.gender = gender
  actor.movies = formatted_movies
  actor.update()
  return jsonify({
    "success": True,
    "actor": actor.format()
  })
    
   

##MOVIES

#GET /movies
@app.route("/movies", methods=["GET"])
def get_movies():
  movies = Movie.query.all()
  formatted_movies = []
  for movie in movies:
    formatted_movies.append(movie.format())
  return jsonify({
    "success": True,
    "movies": formatted_movies
  })
  
#DELETE /movies/{id}
@app.route("/movies/<int:movie_id>", methods=["DELETE"])
@requires_auth('delete: movies')
def delete_movie(payload, movie_id):
  movie = Movie.query.get(movie_id)
  
  if movie is None:
    abort(404)
    
  movie.delete()
  
  return jsonify({
    "success": True,
    "deleted": movie.id
  })

#POST /movies
@app.route("/movies", methods=["POST"])
@requires_auth('post: movies')
def add_movie(payload):
  request_data = request.get_json()
  
  title = request_data.get("title")
  release_date = request_data.get("release_date")
  actor_ids = request_data.get("actors", [])
  
  casted_actors = []
  
  for actor_id in actor_ids:
    actor = Actor.query.get(actor_id)
    if actor is None:
      abort(404)
    else:
      casted_actors.append(actor)
  
  new_movie = Movie(
    title=title,
    release_date=release_date,
    actors=casted_actors
  )
  
  new_movie.insert()
  
  return jsonify({
    "success": True,
    "movie": new_movie.format()
  })
  
  
#PATCH /movies/{id}
@app.route("/movies/<int:movie_id>", methods=["PATCH"])
@requires_auth('patch: movies')
def update_movie(payload, movie_id):
  movie = Movie.query.get(movie_id)
  
  if not movie:
    abort(404)
    
  title = request.get_json().get("title", movie.title)
  release_date = request.get_json().get("release_date", movie.release_date)
  actors = request.get_json().get("actors", [])
  
  if actors is not None:
    formatted_actors = Actor.query.filter(Actor.id.in_(actors)).all()
  else:
    formatted_actors = movie.actors
    
  movie.title = title
  movie.release_date = release_date
  movie.actors = formatted_actors
  movie.update()
  return jsonify({
    "success": True,
    "movie": movie.format()
  })
   
if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)