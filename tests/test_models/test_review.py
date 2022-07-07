#!/usr/bin/python3
"""
Test for Review Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.review import Review

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''
    @classmethod
    def setUp(cls):
        """Set up for test"""
        cls.rev = Review()
        cls.rev.place_id = "fdgf-dcba"
        cls.rev.user_id = "fdw-adrian"
        cls.rev.text = "Holberton School COL"

    def test_attributes_review(self):
        """ Test if review have attributes."""
        self.assertTrue('id' in self.rev.__dict__)
        self.assertTrue('created_at' in self.rev.__dict__)
        self.assertTrue('updated_at' in self.rev.__dict__)
        self.assertTrue('place_id' in self.rev.__dict__)
        self.assertTrue('text' in self.rev.__dict__)
        self.assertTrue('user_id' in self.rev.__dict__)

    def test_is_subclass_Review(self):
        """test if review is subclass of BaseModel"""
        self.assertTrue(issubclass(self.rev.__class__, BaseModel), True)


    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.rev

if __name__ == '__main__':
    unittest.main()

