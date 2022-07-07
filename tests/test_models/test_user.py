#!/usr/bin/python3
"""
Test for User Class
"""
import unittest
import pep8

from models.base_model import BaseModel
from models.user import User

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    '''
    Testing class
    '''

    @classmethod
    def setUpClass(cls):
        """ Set up for test. """
        cls.user = User()
        cls.user.first_name = "Adrian"
        cls.user.last_name = "Hernandez"
        cls.user.email = "1214@holbertonschool.com"
        cls.user.password = "**SHA256(secret)**"

    def test_attributes_User(self):
        """ Test if User have attributes"""
        self.assertTrue('id' in self.user.__dict__)
        self.assertTrue('created_at' in self.user.__dict__)
        self.assertTrue('updated_at' in self.user.__dict__)
        self.assertTrue('first_name' in self.user.__dict__)
        self.assertTrue('last_name' in self.user.__dict__)
        self.assertTrue('email' in self.user.__dict__)
        self.assertTrue('password' in self.user.__dict__)

    def test_is_subclass_User(self):
        """Test if User is subclass of Basemodel."""
        self.assertTrue(issubclass(self.user.__class__, BaseModel), True)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

if __name__ == '__main__':
    unittest.main()

