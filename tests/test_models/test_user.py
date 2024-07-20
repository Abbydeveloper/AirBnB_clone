#!/usr/bin/python3
"""models/user.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.user import User

class TestUser(unittest.TestCase):
    """Unittests for testing the User class"""

    def test_instantiation(self):
        self.assertEqual(User, type(User()))
        self.assertIn(User(), models.storage.all().values())

        self.assertEqual(str, type(User().id))
        self.assertEqual(datetime, type(User().created_at))
        self.assertEqual(datetime, type(User().updated_at))

        self.assertEqual(str, type(User.email))

        self.assertEqual(str, type(User.password))

        self.assertEqual(str, type(User.first_name))

        self.assertEqual(str, type(User.last_name))

        user1 = User()
        sleep(0.08)
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)
        self.assertLess(user1.created_at, user2.created_at)
        self.assertLess(user1.updated_at, user2.updated_at
