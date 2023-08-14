#!/usr/bin/python3
""" test console """

import unittest
from console import HBNBCommand
import console
from unittest.mock import patch
from io import StringIO
from models import storage
import models
from models.base_model import BaseModel
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models.review import Review
from models.amenity import Amenity

classes = {
        "BaseModel": BaseModel,
        "Place": Place,
        "City": City,
        "State": State,
        "User": User,
        "Review": Review,
        "Amenity": Amenity}
class TestConsole(unittest.TestCase):
    """ console test cases"""

    def test_console_doc(self):
        '''test docs of console module and HBNBcommand class'''

        self.assertEqual(HBNBCommand.__doc__, '''hbnb class for the cmd''')
        self.assertEqual(console.__doc__, '''console module contains the \
entry point of the command interpreter''')

    def test_empty_line(self):
        '''tests the output of a new line in the console'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
        text = f.read()
        self.assertEqual(text, "")

    def test_help_commands(self):
        '''test the output of help command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help create")
        text = f.getvalue()

        self.assertEqual(text, "create an instance of a class\n")

        with patch('sys.stdout', new=StringIO()) as o:
            HBNBCommand().onecmd("help quit")
        text = o.getvalue()

        self.assertEqual(text, "Quit command to exit the program\n\n")

    def test_invalid_class(self):
        '''test invalid class with a command'''

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create hellp")
        text = f.getvalue()
        self.assertEqual(text, "** class doesn't exist **\n")

    def test_update(self):
        m = models.base_model.BaseModel()
        m.name = "someone"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create hellp")
        text = f.getvalue()
        self.assertTrue(hasattr(m, 'name'))

    def test_missing_id(self):
        '''test a command that accepts id, without id'''

        with patch('sys.stdout', new=StringIO()) as o:
            HBNBCommand().onecmd("show User")
        text = o.getvalue()

        self.assertEqual(text, "** instance id missing **\n")

    def test_all(self):
        m = models.base_model.BaseModel()
        m.name = "someone"
        m.id = "10"
        m.created_at = "2017-06-14T22:31:03.285259"
        m.updated_at = "2017-06-14T22:31:03.285259"

        for cls in classes.keys():
            with patch('sys.stdout', new=StringIO()) as f:
                line = HBNBCommand().precmd(f"{cls}.all()")
                HBNBCommand().onecmd(line)
            text = f.getvalue()
            self.assertIn(f"[{cls}]", text)
    def test_all(self):
        for cls in classes.keys():
            m = classes[cls]()
            with patch('sys.stdout', new=StringIO()) as f:
                line = HBNBCommand().precmd(f"{cls}.count()")
                HBNBCommand().onecmd(line)
            text = f.getvalue()
            self.assertEqual(1, text)
