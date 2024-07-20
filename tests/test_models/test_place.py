#!/usr/bin/python3
"""models/place.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.place import Place

class TestPlace(unittest.TestCase):
    """Unittests for testing the {;ace class"""

    def test_instantiation(self):
        self.assertEqual(Place, type(Place()))
        self.assertIn(Place(), models.storage.all().values())

        self.assertEqual(str, type(Place().id))
        self.assertEqual(datetime, type(Place().created_at))
        self.assertEqual(datetime, type(Place().updated_at))

        self.assertEqual(str, type(Place.city_id))

        self.assertEqual(str, type(Place.user_id))

        self.assertEqual(str, type(Place.name))

        self.assertEqual(str, type(Place.description))

        self.assertEqual(int, type(Place.number_bathrooms))

        self.assertEqual(int, type(Place.number_rooms))

        self.assertEqual(int, type(Place.max_guest))

        self.assertEqual(int, type(Place.price_by_night))

        self.assertEqual(float, type(Place.latitude))

        self.assertEqual(float, type(Place.longitude))

        self.assertEqual(list, type(Place.amenity_ids)

        place1 = Place()
        sleep(0.08)
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)
        self.assertLess(place1.created_at, place2.created_at)
        self.assertLess(place1.updated_at, place2.updated_at)
