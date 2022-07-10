import datetime
import json
import os
import unittest
from flask import (abort,jsonify,request)
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from models import setup_db, Actor, Movie

DIRECTOR_TOKEN = os.environ.get('DIRECTOR_TOKEN')
ASSISTANT_TOKEN = os.environ.get('ASSISTANT_TOKEN')
PRODUCER_TOKEN = os.environ.get('PRODUCER_TOKEN')
INVALID_TOKEN = os.environ.get('INVALID_TOKEN')

def generate_auth_header(token):
    return {
        'Authorization': 'Bearer ' + token
    }

class UnitTestCase(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = os.environ.get('DATABASE_URL')
        setup_db(self.app)
        
        self.test_actor = {
            "name": "Leonardo DiCaprio",
            "age": 47,
            "gender": "Male"
        }
        
        self.test_actor_bad = {
            "name": "Brad Pitt",
            "age": 58,
            "gender": "Male",
            "movies": [6,7,8]
        }
        
        self.test_movie = {
            "title": "Titanic",
            "release_date": "1995",
        }
        
        self.test_movie_bad = {
            "name": "Toy Story 4",
        }
        
        self.actor_update = {   
            "movies": [1]
        }
        
        self.actor_update_bad = {
            "age": 76
        }
        
        self.movie_update = {
            "title": "Titanic 2",
            "actors": [1]
        }
        
        self.movie_update_bad = {
        }
        
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        
    def tearDown(self):
        pass
    
    ## ENDPOINT TESTS
    
    def test_add_actor(self):
        res = self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["actor"]["name"], "Leonardo DiCaprio")
    
    def test_add_actor_error(self):
        res = self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor_bad)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        
    def test_add_movie(self):
        res = self.client().post("/movies", headers=generate_auth_header(PRODUCER_TOKEN), json=self.test_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data["movie"]["title"], "Titanic")
        
    def test_add_movie_error(self):
        res = self.client().post("/movies", headers=generate_auth_header(PRODUCER_TOKEN), json=self.test_movie_bad)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        
    def test_get_actors(self):
        res = self.client().get("/actors", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_get_actors_error(self):
        res = self.client().get("/actors/", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
        
    def test_get_movies(self):
        res = self.client().get("/movies", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
    
    def test_get_movies_error(self):
        res = self.client().get("/movies/all", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
    def test_update_actor(self):
        self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor)
        self.client().post("/movies", headers=generate_auth_header(PRODUCER_TOKEN), json=self.test_movie)
        res = self.client().patch("/actors/1", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.actor_update)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data["actor"]["movies"], [1])
        
    def test_update_actor_error(self):
        res = self.client().patch("/actors/56", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.actor_update_bad)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_update_movie(self):
        self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor)
        self.client().post("/movies", headers=generate_auth_header(PRODUCER_TOKEN), json=self.test_movie)
        res = self.client().patch("/movies/1", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.movie_update)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data["movie"]["actors"], [1])
        self.assertEqual(data["movie"]["title"], "Titanic 2")
        
    def test_update_movie_error(self):
        res = self.client().patch("/movies/7", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.movie_update_bad)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    def test_delete_actor(self):
        self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor)
        res = self.client().delete("/actors/1", headers=generate_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_delete_actor_error(self):
        res = self.client().delete("/actors/5", headers=generate_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        
    def test_delete_movie(self):
        self.client().post("/movies", headers=generate_auth_header(PRODUCER_TOKEN), json=self.test_movie)
        res = self.client().delete("/movies/1", headers=generate_auth_header(PRODUCER_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        
    def test_delete_movie_error(self):
        res = self.client().delete("/movies/8", headers=generate_auth_header(PRODUCER_TOKEN))
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
    
    ## RBAC TESTS
    
    def test_assistant_valid_auth(self):
        res = self.client().get("/movies", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        
        res = self.client().get("/actors", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)

        
    def test_assistant_invalid_auth(self):
        res = self.client().post("/actors", headers=generate_auth_header(ASSISTANT_TOKEN), json=self.test_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        
        res = self.client().delete("/actors/1", headers=generate_auth_header(ASSISTANT_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        
    
    def test_director_valid_auth(self):
        res = self.client().post("/actors", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        res = self.client().delete("/actors/1", headers=generate_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
      
    def test_director_invalid_auth(self):
        res = self.client().post("/movies", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_movie)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)
        
    def test_producer_valid_auth(self):
        res = self.client().post("/movies", headers=generate_auth_header(DIRECTOR_TOKEN), json=self.test_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        res = self.client().delete("/movies/1", headers=generate_auth_header(DIRECTOR_TOKEN))
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        
    def test_invalid_token(self):
        res = self.client().post("/actors", headers=generate_auth_header(INVALID_TOKEN), json=self.test_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
    
    #def producer_invalid_auth(self):
        

        
    

        

if __name__ == "__main__":
    unittest.main()