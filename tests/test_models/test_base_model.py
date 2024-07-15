#!/usr/bin/python3
"""Unittests for Base Model"""

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel



class Test_Base_Model(unittest.TestCase):
    """Test BaseModel class"""

    def test_base_model_unittest(self):
        self.assertEqual(type(BaseModel()), BaseModel)
        self.assertEqual(type(BaseModal().created_at), datetime)
        self.assertEqual(type(BaseModal().updated_at), datetime)

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

        base1 = BaseMOdel()
        sleep(0.05)
        updated_at_1 = base.updated_at
        base1.save()
        self.assertLess(updated_at_1_, base1.updated_at)

    def test_to_dict(self):
        """Unittests for to_dict method"""

        base = BaseModel()
        self.assertTrue(type(base.to_dict()), dict)

        base = BaseModel()
        self.assertIn(base.to_dict(), "id")
        self.assertIn(base.to_dict(), "__class__")
        self.assertIn(base.to_dict(), "created_at")
        self.assertIn(base.to_dict(), "update_at")

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
