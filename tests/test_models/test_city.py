#!/usr/bin/python3
'''test the class City'''

import unittest
from models.base_model import BaseModel
from models.city import City
import models
import datetime
'''modules'''


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of City'''
        m = City()
        m.save()
        m.name = 'someone'
        m.state_id = "29"

        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["name"]), str)
        self.assertEqual(d["state_id"], "29")

    def test_save(self):
        ''' test City save method '''
        m = City()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "City",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                "state_id": 100,
                }
        m = City(**dict_obj)
        self.assertEqual(m.__class__.__name__, "City")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.state_id), int)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")

    def test_instances(self):
        """Tests instantiation of City class."""
        model1 = City()
        self.assertEqual(str(type(model1)), "\
<class 'models.city.City'>")
        self.assertIsInstance(model1, City)
        self.assertTrue(issubclass(type(model1), BaseModel))

    def test_attributes(self):
        '''tests attibutes of City'''

        model1 = City()
        model1.name = 'someone'
        model1.state_id = 100
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''city class module'''
        self.assertEqual(models.city.__doc__, doc)

        class_doc = '''city class indicates city'''
        self.assertEqual(City.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of City attributes'''

        m = City()
        m.name = 'someone'
        m.state_id = "29"
        m.save()
        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertTrue(type(m.state_id), int)
        self.assertTrue(type(m.name), str)

    def test_str(self):
        '''test City sting representation'''

        m = City()
        m.id = "10"
        string_m = "[City] (10)"
        self.assertIn(string_m, str(m))
