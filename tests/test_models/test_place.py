#!/usr/bin/python3
'''test the class Place'''
import unittest
from models.place import Place
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of Place class."""
        p = Place()
        self.assertEqual(str(type(p)), "<class 'models.place.Place'>")
        self.assertIsInstance(p, Place)
        self.assertTrue(issubclass(type(p), BaseModel))
