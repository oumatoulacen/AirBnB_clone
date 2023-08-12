#!/usr/bin/python3
'''test the class User'''

import unittest
from models.user import User
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of Amenity class."""
        u = User()
        self.assertEqual(str(type(u)), "<class 'models.user.User'>")
        self.assertIsInstance(u, User)
        self.assertTrue(issubclass(type(u), BaseModel))
