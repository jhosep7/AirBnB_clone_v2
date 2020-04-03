#!/usr/bin/python
"""Unittests for DBStorage class in AirBnb_Clone_v2"""
import unittest
import pep8
import os
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
import MySQLdb


class TestDBStorage(unittest.TestCase):
    '''Testing the DBStorage'''

    def test_pep8_conformance_db_storage(self):
        """Test that models/engine/db_storage.py has correct PEP8 style."""
        pep8st = pep8.StyleGuide(quiet=True)
        result = pep8st.check_files(['models/engine/db_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "There are code style errors.")
