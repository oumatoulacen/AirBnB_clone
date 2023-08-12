#!/usr/bin/python3
'''test the class BaseModel'''
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of Amenity class."""
        m = Amenity()
        self.assertEqual(str(type(m)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(m, Amenity)
        self.assertTrue(issubclass(type(m), BaseModel))
