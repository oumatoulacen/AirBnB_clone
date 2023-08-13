#!/usr/bin/python3
'''test the class Amenity'''

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
import models
import datetime
'''modules'''


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of Amenity'''
        m = Amenity()
        m.save()
        m.name = 'someone'
        m.number = 90
        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["name"]), str)
        self.assertTrue(type(d["number"]), int)

    def test_save(self):
        ''' test Amenity save method '''
        m = Amenity()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "Amenity",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                "number": 100,
                }
        m = Amenity(**dict_obj)
        self.assertEqual(m.__class__.__name__, "Amenity")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.number), int)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")

    def test_instances(self):
        """Tests instantiation of Amenity class."""
        model1 = Amenity()
        self.assertEqual(str(type(model1)), "\
<class 'models.amenity.Amenity'>")
        self.assertIsInstance(model1, Amenity)
        self.assertTrue(issubclass(type(model1), BaseModel))

    def test_attributes(self):
        '''tests attibutes of Amenity'''

        model1 = Amenity()
        model1.name = 'someone'
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''amenity class module'''
        self.assertEqual(models.amenity.__doc__, doc)

        class_doc = '''amenity class'''
        self.assertEqual(Amenity.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of Amenity attributes'''

        m = Amenity()
        m.name = "someone"
        m.save()
        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.name), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)

    def test_str(self):
        '''test Amenity sting representation'''

        m = Amenity()
        m.id = "10"
        string_m = "[Amenity] (10)"
        self.assertIn(string_m, str(m))

