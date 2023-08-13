#!/usr/bin/python3
'''test the class BaseModel'''
import unittest
from models.base_model import BaseModel
from models.place import Place
import models
import datetime
'''modules'''


class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of Place'''
        m = Place()
        m.city_id = "10"
        m.user_id = "10"
        m.name = "palas"
        m.desciption = "very good"
        m.number_rooms = 4
        m.number_bathrooms = 3
        m.max_guest = 8
        m.price_by_night = 100
        m.latitude = 2.0
        m.longitude = 30.0
        m.amenity_ids = []

        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["city_id"]), str)
        self.assertTrue(type(d["number_rooms"]), int)
        self.assertEqual(d["user_id"], "10")
        self.assertEqual(d["city_id"], "10")
        self.assertEqual(d["name"], "palas")
        self.assertEqual(d["desciption"], "very good")
        self.assertEqual(d["number_rooms"], 4)
        self.assertEqual(d["number_bathrooms"], 3)
        self.assertEqual(d["max_guest"], 8)
        self.assertEqual(d["price_by_night"], 100)
        self.assertEqual(d["latitude"], 2.0)
        self.assertEqual(d["longitude"], 30.0)
        self.assertEqual(d["amenity_ids"], [])

    def test_save(self):
        ''' test Place save method '''
        m = Place()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "Place",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                "number": 100,
                }
        m = Place(**dict_obj)
        self.assertEqual(m.__class__.__name__, "Place")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.number), int)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")

    def test_instances(self):
        """Tests instantiation of Place class."""
        model1 = Place()
        self.assertEqual(str(type(model1)), "\
<class 'models.place.Place'>")
        self.assertIsInstance(model1, Place)
        self.assertTrue(issubclass(type(model1), BaseModel))

    def test_attributes(self):
        '''tests attibutes of Place'''

        model1 = Place()
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''place class module'''
        self.assertEqual(models.place.__doc__, doc)

        class_doc = '''place clace'''
        self.assertEqual(Place.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of Place attributes'''

        m = Place()
        m.city_id = "10"
        m.user_id = "10"
        m.name = "palas"
        m.desciption = "very good"
        m.number_rooms = 4
        m.number_bathrooms = 3
        m.max_guest = 8
        m.price_by_night = 100
        m.latitude = 2.0
        m.longitude = 30.0
        m.amenity_ids = []

        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["city_id"]), str)
        self.assertTrue(type(d["number_rooms"]), int)
        self.assertTrue(type(d["user_id"]), str)
        self.assertTrue(type(d["city_id"]), str)
        self.assertTrue(type(d["name"]), str)
        self.assertTrue(type(d["desciption"]), str)
        self.assertTrue(type(d["number_rooms"]), int)
        self.assertTrue(type(d["number_bathrooms"]), int)
        self.assertTrue(type(d["max_guest"]), int)
        self.assertTrue(type(d["price_by_night"]), int)
        self.assertTrue(type(d["latitude"]), float)
        self.assertTrue(type(d["longitude"]), float)
        self.assertTrue(type(d["amenity_ids"]), list)

        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)

    def test_str(self):
        '''test Place sting representation'''

        m = Place()
        m.id = "10"
        string_m = "[Place] (10)"
        self.assertIn(string_m, str(m))
