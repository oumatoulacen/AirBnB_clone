#!/usr/bin/python3
'''test the class BaseModel'''
import unittest
from models.base_model import BaseModel
from models.state import State
import models
import datetime
'''modules'''


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of State'''
        m = State()
        m.save()
        m.name = 'someone'
        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["name"]), str)

    def test_save(self):
        ''' test State save method '''
        m = State()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "State",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                }
        m = State(**dict_obj)
        self.assertEqual(m.__class__.__name__, "State")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")

    def test_instances(self):
        """Tests instantiation of State class."""
        model1 = State()
        self.assertEqual(str(type(model1)), "\
<class 'models.state.State'>")
        self.assertIsInstance(model1, State)
        self.assertTrue(issubclass(type(model1), BaseModel))

    def test_attributes(self):
        '''tests attibutes of State'''

        model1 = State()
        model1.name = 'someone'
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''state class model'''
        self.assertEqual(models.state.__doc__, doc)

        class_doc = '''state class indicates the state'''
        self.assertEqual(State.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of State attributes'''

        m = State()
        m.save()
        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertTrue(type(m.name), str)
    def test_str(self):
        '''test State sting representation'''

        m = State()
        m.id = "10"
        string_m = "[State] (10)"
        self.assertIn(string_m, str(m))

