#!/usr/bin/python3
'''test the class BaseModel'''
import unittest
from models.base_model import BaseModel
import uuid
'''unitest, models module'''


class TestBaseModel(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_instances(self):
        """Tests instantiation of BaseModel class."""
        model1 = BaseModel()
        self.assertEqual(str(type(model1)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(model1, BaseModel)
        self.assertTrue(issubclass(type(model1), BaseModel))
