#!/usr/bin/python3
"""
Test for Amenity Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.amenity import Amenity

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    """
    Testing class
    """
    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.amenity = Amenity()
        cls.amenity.name = "Breakfast"

    def test_docstring_Amenity(self):
        """ Testing for docstrings. """
        self.assertIsNotNone(Amenity.__doc__)

    def test_attributes_Amenity(self):
        """Testing if amenity have attibutes."""
        self.assertTrue('id' in self.amenity.__dict__)
        self.assertTrue('created_at' in self.amenity.__dict__)
        self.assertTrue('updated_at' in self.amenity.__dict__)
        self.assertTrue('name' in self.amenity.__dict__)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.amenity

if __name__ == '__main__':
    unittest.main()
