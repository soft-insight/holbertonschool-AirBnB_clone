#!/usr/bin/python3
"""
Test for city Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.city import City

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''
    @classmethod
    def setUp(cls):
        """set up for test"""
        cls.city = City()
        cls.city.name = "LA"
        cls.city.state_id = "CA"

    def test_attributes_City(self):
        """ Testing if City have attributes."""
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_is_subclass_City(self):
        """ if City is subclass of Basemodel."""
        self.assertTrue(issubclass(self.city.__class__, BaseModel), True)

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.city

if __name__ == '__main__':
    unittest.main()
