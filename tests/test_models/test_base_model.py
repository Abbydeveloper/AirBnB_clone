#!/usr/bin/python3
"""Unittests for Base Model"""

import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.base_model import BaseModel



class Test_Base_Model(unittest.TestCase):
    """Test BaseModel class"""

    def test_base_model_unittest(self):
        self.assertEqual(type(BaseModel()), BaseModel)
        self.assertEqual(type(BaseModel().created_at), datetime)
        self.assertEqual(type(BaseModel().updated_at), datetime)

        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    @classmethod
    def save_setup(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_base_model_save(self):
        """
        Unittests for testing save method"""

        base1 = BaseModel()
        sleep(0.05)
        updated_at_1 = base1.updated_at
        self.assertEqual(updated_at_1, datetime.utcnow())
        base1.save()
        updated_at_2 = base1.updated_at
        self.assertLess(updated_at_1, updated_at_2)
        sleep(0.05)
        base1.save()
        self.assertLess(updated_at_1, base1.updated_at)

    def test_to_dict(self):
        """Unittests for to_dict method"""

        base = BaseModel()
        self.assertTrue(type(base.to_dict()), dict)

        base = BaseModel()
        self.assertIn("id", base.to_dict())
        self.assertIn("__class__", base.to_dict())
        self.assertIn("created_at", base.to_dict())
        self.assertIn("updated_at", base.to_dict())

    def test_str(self):
        date = datetime.today()
        date_repr = repr(date)
        base = BaseModel()
        base.id = "123"
        base.created_at = base.updated_at = date
        base_str = base.__str__()
        self.assertIn("[BaseModel] (123)", base_str)
        self.assertIn("'id': '123'", base_str)
        self.assertIn("'updated_at': " + date_repr, base_str)
        self.assertIn("'created_at': " + date_repr, base_str)
