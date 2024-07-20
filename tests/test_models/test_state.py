#!/usr/bin/python3
"""models/state.py unittests"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.state import State

class TestState(unittest.TestCase):
    """Unittests for testing the State class"""

    def test_instantiation(self):
        self.assertEqual(State, type(State()))
        self.assertIn(State(), models.storage.all().values())

        self.assertEqual(str, type(State().id))
        self.assertEqual(datetime, type(State().created_at))
        self.assertEqual(datetime, type(State().updated_at))

        self.assertEqual(str, type(State.name))

        state1 = State()
        sleep(0.08)
        state2 = State()
        self.assertNotEqual(state1.id, state2.id)
        self.assertLess(state1.created_at, state2.created_at)
        self.assertLess(state1.updated_at, state2.updated_at)
