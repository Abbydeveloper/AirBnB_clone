#!/usr/bin/python3
"""models/city.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City

class TestCity(unittest.TestCase):
    """Unittests for testing the City class"""

    def test_instantiation(self):
        self.assertEqual(City, type(City()))
        self.assertIn(City(), models.storage.all().values())

        self.assertEqual(str, type(City().id))
        self.assertEqual(datetime, type(City().created_at))
        self.assertEqual(datetime, type(City().updated_at))

        self.assertEqual(str, type(City.state_id))

        self.assertEqual(str, type(City.name))

        city1 = City()
        sleep(0.08)
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)
        self.assertLess(city1.created_at, city2.created_at)
        self.assertLess(city1.updated_at, city2.updated_at)
