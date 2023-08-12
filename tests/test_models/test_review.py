#!/usr/bin/python3
'''test the class review'''

import unittest
from models.review import Review
from models.base_model import BaseModel
import uuid
'''unitest, models, uuid modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of Review class."""
        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(type(r), BaseModel))
