#!/usr/bin/python3
"""models/review.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.review import Revoew

class TestReview(unittest.TestCase):
    """Unittests for testing the Review class"""

    def test_instantiation(self):
        self.assertEqual(Review, type(Review()))
        self.assertIn(Review(), models.storage.all().values())

        self.assertEqual(str, type(Review().id))
        self.assertEqual(datetime, type(Review().created_at))
        self.assertEqual(datetime, type(Review().updated_at))

        self.assertEqual(str, type(Review.place_id))

        self.assertEqual(str, type(Review.user_id))

        self.assertEqual(str, type(Review.text))

        review1 = Review()
        sleep(0.08)
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)
        self.assertLess(review1.created_at, review2.created_at)
        self.assertLess(review1.updated_at, review2.updated_at)
