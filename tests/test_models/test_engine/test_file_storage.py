#!/usr/bin/python3
"""Define unittests for models/engine package"""
import os
import json
import models
import unittest


class Test_engine(unittest.TestCase):
    """Unittests for FileStorage class"""

    def test_filestorage(self):
        self.assertEqual(type(FileStorage()), FileStorage)

        with self.assertRaises(TypeError):
            FileStorage(None)

        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

        self.assertEqual(type(models.storage), FileStorage)

    @classmethod
    def Setup(self):
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
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_reload(self):
        self.assertRaises(FileNotFoundError, models.storage.reload())

        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_new(self):
        base = BaseModel()
        models.storage = new(base)
        self.assertIn("BaseModel." + base.id, models.storage.all().keys())

    def test_save(self):
        base = BaseModel()
        models.storage.new(base)
        models.storage.save()
        save_text = ""
        with open("file.json", mode="r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base.id, save_text)
