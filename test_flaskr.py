import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from models import setup_db, Movie, Actor, db

class CastingAgencyTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        setup_db(self.app)

        self.casting_assistant_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTIyNzY2ODcwMjQ5NDY3MTY1NjQiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDk1MTY4LCJleHAiOjE2MDcxMDIzNjgsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.VU071gdJRbQA5S4g_5khWg8Ez4eMV-G1C-hP4PE6x--PNTIu_46J26UoMRVdrDyCgBlfbsM862yYz1x_mESBllr_ViT0fPEG8VK8Bu-uPFHsMlIMP6wuXZMD0xhULTqWpfjWTFRANi1r7mv2xvMzzm2dbLgWHhOKgYfxY9-NV1g9692ctw06TeA7crZ2R6R-6s09wLs6zGLrC8FQwadNolEG_lXxLCFQtKndQaN_IOtD_wmihWZaiDG-4P3NdD6hvvBPzafhtGzK90jgMmGi6pJLsDEn2jRs1NYeZElgNhR5jqVXYM0I_9-i-xJg1O8FSAX62uBy2UZSCW7HD3Oqig'
        }

        self.casting_director_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTQyNTk1MjgyOTkwNjE3OTY4ODgiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDk1MDkyLCJleHAiOjE2MDcxMDIyOTIsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJkZWxldGU6YWN0b3JzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwidmlldzphY3RvcnMiLCJ2aWV3Om1vdmllcyJdfQ.Ihuw3GyELHtsT3LZ_nxODd0VY9_HDRToxnX7dXYgbIdrXfQ1cZM2IMrdvNTOOO6Plnoc3yCdIWuBHqDA9ATEQ87vXH0MZelhBT2nRPXYGKsJDEknCaLQTZ0esR_zbU-q-RbDtIKp5ugpcl-tt0N3OB_1p8cbla6TMLl4_OwimryzTXtohQUTeOhB-WXwUnDh3K5ixUaBwIFdty0Of9mIi5ITtQ46laHxVDHJVqjeceEtMUQI_2JXMUBbSd1xIuXnbFUykXN_1V4gRHdPL8y0C1mkXkqBLFPkIpstca8v9PfWlJtKZnPDEsUv7rvitLChEZCFm9X44Rq2EVEvUzIjww'
        }

        self.executive_producer_header = {
            'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InJVaEVvLUpfVDRscEVuclRIVW5zTiJ9.eyJpc3MiOiJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vIiwic3ViIjoiZ29vZ2xlLW9hdXRoMnwxMTc2OTE3MjcyMDc3OTcxNTczMTUiLCJhdWQiOlsiY2Fwc3RvbmUiLCJodHRwczovL2Rldi1mYTI1cHhqOS51cy5hdXRoMC5jb20vdXNlcmluZm8iXSwiaWF0IjoxNjA3MDk1MDE2LCJleHAiOjE2MDcxMDIyMTYsImF6cCI6IjhnNlFHTnRSNDZsa25SQ1djbDcwZHU2NzdqWTUxU2JOIiwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInBlcm1pc3Npb25zIjpbImFkZDphY3RvcnMiLCJhZGQ6bW92aWVzIiwiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.V7TffwFTHCppL42OqM50kP6Bt7YYwMIrzJJHaeYRuUaxkYGQQ5DcG3bQmpt8WXRK3DL0giDEv7qJYhiJHtFb6IsUrRJNqGbaNk3rYNccIAy1e7MO1vsHrWYgqFVuSaRJRp9YsTBR3XA8JVBrxL2P3Do_0egQKZvZ0uTYj57HbmIPp3oOt5DHelQh4Rgxd_TJmdbK7HVNYm5SuzDOCiuLl8T95apCyPQfH_Wd_3MwGOglJd1Rgvv_z9-FZaPALhi2DM9VbmPNqaPYbz4KCx8EZSul0JMupOJ5qQqZQ6OdK3AaezHskLB_K_uGJ3BBGN-r4J9SC6XwCNl3d5mAJ0ypGA'
        }

        self.movie = {
            'title': 'The Godfather',
            "release_date": "2020-01-02",
            "genre": "romantic"
        }

        self.new_movie = {
            "genre": "romantic",
            'title': 'Toy Story 4',
            "release_date": "2020-01-02"
        }

        self.actor = {
            'name': 'Leonardo DiCaprio',
            'age': '46',
            'gender': 'Male'
        }

        self.new_actor = {
            'name': 'Meryl Streep',
            'age': '71',
            'gender': 'Female'
        }


        # binds the app to the current context
        with self.app.app_context():
            self.db = db
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    

        #Seed test data
        self.client().post('/movies', json=self.movie, headers=self.executive_producer_header)
        self.client().post('/actors', json=self.actor, headers=self.executive_producer_header) 

   
    def tearDown(self):
        """Executed after reach test"""
        self.db.drop_all()
        pass

# Test POST Actor
    def test_post_actors_public(self):
        res = self.client().post('/actors', json=self.new_actor)

        self.assertEqual(res.status_code, 401)

    def test_post_actors_assistant(self):
        res = self.client().post('/actors', json=self.new_actor, headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_post_actors_director(self):
        original_count = len(Actor.query.all())

        res = self.client().post('/actors', json=self.new_actor, headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertGreater(data['actor_id'], 0)

    def test_post_actors_producer(self):
        original_count = len(Actor.query.all())

        res = self.client().post('/actors', json=self.new_actor, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertGreater(data['actor_id'], 0)

    # Test POST Movie
    def test_post_movies_public(self):
        res = self.client().post('/movies', json=self.new_movie)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_assistant(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_director(self):
        res = self.client().post('/movies', json=self.new_movie, headers=self.casting_director_header)

        self.assertEqual(res.status_code, 401)

    def test_post_movies_producer(self):
        original_count = len(Movie.query.all())

        res = self.client().post('/movies', json=self.new_movie, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertGreater(data['movie_id'], 0)
    

    # Test GET Actors
    def test_get_actors_public(self):
        res = self.client().get('/actors')

        self.assertEqual(res.status_code, 401)

    def test_get_actors_assistant(self):
        res = self.client().get('/actors', headers=self.casting_assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_actors_director(self):
        res = self.client().get('/actors', headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    def test_get_actors_producer(self):
        res = self.client().get('/actors', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['actors']))

    # Test GET Movies
    def test_get_movies_public(self):
        res = self.client().get('/movies')

        self.assertEqual(res.status_code, 401)

    def test_get_movies_assistant(self):
        res = self.client().get('/movies', headers=self.casting_assistant_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_get_movies_director(self):
        res = self.client().get('/movies', headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    def test_get_movies_producer(self):
        res = self.client().get('/movies', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(len(data['movies']))

    

    # Test PATCH Actor
    def test_patch_actors_public(self):
        res = self.client().patch('/actors/1', json={'age': "71"})

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_assistant(self):
        res = self.client().patch('/actors/1', json={'age': "71"}, headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_actors_director(self):
        res = self.client().patch('/actors/1', json={'age': "71"}, headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_actors_producer(self):
        res = self.client().patch('/actors/1', json={'age': "71"}, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)



    # Test PATCH Movie
    def test_patch_movies_public(self):
        res = self.client().patch('/movies/1', json={'title': "The Witch"})

        self.assertEqual(res.status_code, 401)

    def test_patch_movies_assistant(self):
        res = self.client().patch('/movies/1', json={'title': "The Witch"}, headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_patch_movies_director(self):
        res = self.client().patch('/movies/1', json={'title': "The Witch"}, headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_patch_movies_producer(self):
        res = self.client().patch('/movies/1', json={'title': "The Witch"}, headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    

    

    # Test DELETE Actor
    def test_delete_actors_public(self):
        res = self.client().delete('/actors/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_actors_assistant(self):
        res = self.client().delete('/actors/1', headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_actors_director(self):
        res = self.client().delete('/actors/1', headers=self.casting_director_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actors_producer(self):
        res = self.client().delete('/actors/1', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    # Test DELETE Movie
    def test_delete_movies_public(self):
        res = self.client().delete('/movies/1')

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_assistant(self):
        res = self.client().delete('/movies/1', headers=self.casting_assistant_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_director(self):
        res = self.client().delete('/movies/1', headers=self.casting_director_header)

        self.assertEqual(res.status_code, 401)

    def test_delete_movies_producer(self):
        res = self.client().delete('/movies/1', headers=self.executive_producer_header)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

 


if __name__ == "__main__":
    unittest.main()