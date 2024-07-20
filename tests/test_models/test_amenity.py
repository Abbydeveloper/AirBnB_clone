#!/usr/bin/python3
"""models/amenity.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unittests for testing the Amenity class"""

    def test_instantiation(self):
        self.assertEqual(Amenity, type(Amenity()))
        self.assertIn(Amenity(), models.storage.all().values())

        self.assertEqual(str, type(Amenity().id))
        self.assertEqual(datetime, type(Amenity().created_at))
        self.assertEqual(datetime, type(Amenity().updated_at))

        self.assertEqual(str, type(Amenity.name))

        amenity1 = Amenity()
        sleep(0.08)
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)
        self.assertLess(amenity1.created_at, amenity2.created_at)
        self.assertLess(amenity1.updated_at, amenity2.updated_at)
