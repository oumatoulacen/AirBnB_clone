#!/usr/bin/python3
'''test the Review class'''
import unittest
from models.base_model import BaseModel
from models.review import Review
import models
import datetime
'''modules'''


class TestBaseModel(unittest.TestCase):
    """Test Cases for the Review class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_to_dict(self):
        '''test to_dect method of Review'''
        m = Review()
        m.save()
        m.place_id = '10'
        m.user_id = '9'
        m.text = "good"
        m.name = "someone"
        d = m.to_dict()
        self.assertTrue(type(d["id"]), str)
        self.assertTrue(type(d["created_at"]), str)
        self.assertTrue(type(d["updated_at"]), str)
        self.assertTrue(type(d["name"]), str)
        self.assertTrue(type(d["place_id"]), int)
        self.assertTrue(type(d["user_id"]), int)
        self.assertTrue(type(d["text"]), str)

    def test_save(self):
        ''' test Review save method '''
        m = Review()
        updated = m.updated_at
        m.save()
        self.assertNotEqual(updated, m.updated_at)

    def test_instance_from_dict(self):
        dict_obj = {
                '__class__': "Review",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                "place_id": "100",
                "user_id": "66",
                "text": "good"
                }
        m = Review(**dict_obj)
        self.assertEqual(m.__class__.__name__, "Review")
        self.assertEqual(m.id, "10")
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")
        self.assertEqual(m.place_id, "100")
        self.assertEqual(m.user_id, "66")
        self.assertEqual(m.text, "good")

    def test_instances(self):
        """Tests instantiation of Review class."""
        r = Review()
        self.assertEqual(str(type(r)), "<class 'models.review.Review'>")
        self.assertIsInstance(r, Review)
        self.assertTrue(issubclass(type(r), BaseModel))

    def test_attributes(self):
        '''tests attibutes of Review'''

        m = BaseModel()
        m.name = 'someone'
        m.place_id = "100"
        m.user_id = "66"
        m.text = "good"
        for key in m.__dict__.keys():
            self.assertTrue(hasattr(m, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''the review class module'''
        self.assertEqual(models.review.__doc__, doc)

        class_doc = '''review class'''
        self.assertEqual(Review.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of Review attributes'''

        m = Review()
        m.save()
        self.assertTrue(type(m.id), str)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertTrue(type(m.place_id), str)
        self.assertTrue(type(m.user_id), str)
        self.assertTrue(type(m.text), str)

    def test_str(self):
        '''test BaseModel sting representation'''

        m = Review()
        m.id = "10"
        string_m = "[Review] (10)"
        self.assertIn(string_m, str(m))
