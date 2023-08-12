#!/usr/bin/python3
'''test the class City'''

import unittest
from models.city import City
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of City class."""
        c = City()
        self.assertEqual(str(type(c)), "<class 'models.city.City'>")
        self.assertIsInstance(c, City)
        self.assertTrue(issubclass(type(c), City))
