#!/usr/bin/python3
'''test the class BaseModel'''
import unittest
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.review import Review
from models.user import User
from models.amenity import Amenity
from models.place import Place

from models.engine.file_storage import FileStorage
import models
import datetime
'''modules'''


class TestFileStorage(unittest.TestCase):
    """Test Cases for the BaseModel class."""

    def setUp(self):
        """Sets up test methods."""
        pass

    def tearDown(self):
        """Tears down test methods."""
        pass

    def test_all(self):
        '''test to_dect method of FileStorage'''
        m = FileStorage()
        m.reload()
        dic = m.all()
        self.assertTrue(dic, {})

    def test_reload(self):
        ''' test BaseModel save method '''
        m = FileStorage()
        base = BaseModel()
        place = Place()
        city = City()
        review = Review()
        state = State()
        user = User()
        amenity = Amenity()

        m.new(base)
        m.new(place)
        m.new(city)
        m.new(review)
        m.new(state)
        m.new(user)
        m.new(amenity)
        m.save()
        m.reload()
        self.assertIsInstance(m.all()[f"{base.__class__.__name__}.{base.id}\
"], BaseModel)
        self.assertIsInstance(m.all()[f"{place.__class__.__name__}.{place.id}\
"], Place)
        self.assertIsInstance(m.all()[f"{city.__class__.__name__}.{city.id}\
"], City)
        self.assertIsInstance(m.all()[f"{review.__class__.__name__}.\
{review.id}"], Review)
        self.assertIsInstance(m.all()[f"{state.__class__.__name__}.{state.id}\
"], State)
        self.assertIsInstance(m.all()[f"{user.__class__.__name__}.{user.id}\
"], User)
        self.assertIsInstance(m.all()[f"{amenity.__class__.__name__}.\
{amenity.id}"], Amenity)

    def test_new(self):
        dict_obj = {
                '__class__': "FileStorage",
                "id": "10",
                "created_at": "2022-01-01T10:01:25.123456",
                "updated_at": "2022-01-01T10:01:25.123456",
                "name": "someone",
                "number": 100,
                }
        m = BaseModel(**dict_obj)
        obj = FileStorage()
        obj.new(m)
        self.assertEqual(obj.__class__.__name__, "FileStorage")
        self.assertEqual(m.id, "10")
        self.assertEqual(obj.all()[f"{m.__class__.__name__}.{m.id}"], m)
        self.assertTrue(type(m.created_at), datetime.datetime)
        self.assertTrue(type(m.updated_at), datetime.datetime)
        self.assertEqual(m.name, "someone")

    def test_instances(self):
        """Tests instantiation of FileStorage class."""
        model1 = FileStorage()
        self.assertEqual(str(type(model1)), "\
<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(model1, FileStorage)
        self.assertTrue(issubclass(type(model1), FileStorage))

    def test_attributes(self):
        '''tests attibutes of FileStorage'''

        model1 = FileStorage()
        for key in model1.__dict__.keys():
            self.assertTrue(hasattr(model1, key))

    def test_docs(self):
        '''test docs of module and class'''

        doc = '''a module to Store objects'''
        self.assertEqual(models.engine.file_storage.__doc__, doc)

        class_doc = '''a class that serializes instances to a JSON file
and deserializes JSON file to instances'''
        self.assertEqual(FileStorage.__doc__, class_doc)

    def test_types_of_attr(self):
        '''test type of FileStorage attributes'''

        m = FileStorage()
        self.assertTrue(type(m.all()), dict)
