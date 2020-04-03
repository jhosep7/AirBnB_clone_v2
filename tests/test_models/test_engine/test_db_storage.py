#!/usr/bin/python3
"""tests DB"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from os import getenv

class TestDBStorage(unittest.TestCase):
    '''test DBStorage'''

    @classmethod
    def setUpClass(cls):
        """Class"""
        cls.user = User()
        cls.user.first_name = "Fab"
        cls.user.last_name = "He"
        cls.user.email = "2020@gmail.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """tear down"""
        del cls.user


    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "Not using db")
    def test_DBStorage(self):
        """pep8 """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    @unittest.skipIf(getenv("HBNB_TYPE_STORAGE") != "db",
                     "Not using db")
    def test_all(self):
        """testing all"""
        storage = DBStorage()
        storage.reload()
        dict_len = len(storage.all())
        s = State(name="test_all_state")
        s.save()
        storage.save()
        self.assertIs(len(storage.all()), dict_len + 1)
