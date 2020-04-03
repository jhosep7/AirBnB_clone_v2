#!/usr/bin/python3
"""test for city"""
import unittest
import pep8
import os
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
import models


class TestCity(unittest.TestCase):
    """this will test the city class"""

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

    def tearDown(self):
        """teardown"""
        try:
            os.remove("file.json")
        except Exception:
            pass

    def test_pep8_City(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/city.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_docstring_City(self):
        """checking for docstrings"""
        self.assertIsNotNone(City.__doc__)

    def test_attributes_City(self):
        """chekcing if City have attributes"""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_is_subclass_City(self):
        """test if City is subclass of Basemodel"""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    def test_attribute_types_City(self):
        """test attribute type for City"""
        self.assertEqual(type(self.city.name), str)
        self.assertEqual(type(self.city.state_id), str)

    def test_save_City(self):
        """test if the save works"""
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict_City(self):
        """test if dictionary works"""
        self.assertEqual('to_dict' in dir(self.city), True)

    def test_relation_db(self):
        """ Check relation """
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            my_state = State(name="California")
            my_state.save()
            city = City(name="Arizona", state_id=my_state.id)
            city.save()
            self.assertTrue(city.state == my_state)

    def test_create_db(self):
        """ check create obj"""
        if os.getenv('HBNB_TYPE_STORAGE') == 'db':
            value_a = len(models.storage.all("City"))
            my_state = State(name="California")
            my_state.save()
            my_city = City(name="Arizona", state_id=my_state.id)
            my_city.save()
            self.assertEqual(value_a + 1, len(models.storage.all("City")))
            models.storage.delete(my_city)
            self.assertEqual(value_a, len(models.storage.all("City")))

if __name__ == "__main__":
    unittest.main()
