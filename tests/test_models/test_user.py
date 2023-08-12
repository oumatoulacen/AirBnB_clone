#!/usr/bin/python3
'''test the class BaseModel'''

import unittest
from models.base_model import BaseModel
from models.user import User
import models
import datetime
'''modules'''


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of User'''
        m = User()
        m.save()
        m.email = "@gmail.com"
        m.password = "123"
        m.first_name = "some"
        m.last_name = "one"
        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertEqual(d["first_name"], "some")
        self.assertEqual(d["last_name"], "one")
        self.assertEqual(d["password"], "123")
        self.assertEqual(d["email"], "@gmail.com")

    def test_save(self):
        ''' test User save method '''
        m = User()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "User",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "first_name": "some",
                "last_name": "one",
                "password": 100,
                }
        m = User(**dict_obj)
        self.assertEqual(m.__class__.__name__, "User")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.password), int)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.first_name, "some")
        self.assertEqual(m.last_name, "one")

    def test_instances(self):
        """Tests instantiation of User class."""
        model1 = User()
        self.assertEqual(str(type(model1)), "\
<class 'models.user.User'>")
        self.assertIsInstance(model1, User)
        self.assertTrue(issubclass(type(model1), BaseModel))

    def test_attributes(self):
        '''tests attibutes of User'''

        model1 = User()
        model1.first_name = 'some'
        model1.last_name = 'one'
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = ''' the user class module'''
        self.assertEqual(models.user.__doc__, doc)

        class_doc = '''user class'''
        self.assertEqual(User.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of User attributes'''

        m = User()
        m.save()
        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertTrue(type(m.password), str)
        self.assertTrue(type(m.first_name), str)
        self.assertTrue(type(m.last_name), str)
        self.assertTrue(type(m.email), str)
    def test_str(self):
        '''test User sting representation'''

        m = User()
        m.id = "10"
        string_m = "[User] (10)"
        self.assertIn(string_m, str(m))

