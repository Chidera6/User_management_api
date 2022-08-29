import os
import unittest
import json
from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
from models import Country,User

class userTestCase(unittest.TestCase):
    """This class represents the user test case"""
    def setUp(self):
        """Define test variables and initialize app."""

        self.new_user = {"first_name":"chidera", "last_name":"stella", "email":"dictasteil@gmail.com", "phone":"2349166"}
        
        
     
    def tearDown(self):
        """Executed after each test"""
        pass

    
    def test_get_users(self):
        res = self.client().get("/users")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)        

    def test_get_user_by_id(self):
        res = self.client().get("/users")
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        
    def test_delete_(self):
        res = self.client().delete("/user/20")
        data = json.loads(res.data)
        question = Users.query.filter_by(user_id==user_id).all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_post_question(self):
        res = self.client().post("/create", json=self.new_user)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
    
