#!/usr/bin/python3
'''test the class State'''
import unittest
from models.state import State
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of State class."""
        s = State()
        self.assertEqual(str(type(s)), "<class 'models.state.State'>")
        self.assertIsInstance(s, State)
        self.assertTrue(issubclass(type(s), BaseModel))
