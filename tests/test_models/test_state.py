#!/usr/bin/python3
"""
Test for State Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.state import State

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''
    @classmethod
    def setUpClass(cls):
        """ Set up for test."""
        cls.state = State()
        cls.state.name = "California"

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/state.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_attributes_State(self):
        """ Testing if State have attributes."""
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_is_subclass_State(self):
        """ if State is subclass of BaseModel"""
        self.assertTrue(issubclass(self.state.__class__, BaseModel), True)

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.state

if __name__ == '__main__':
    unittest.main()
