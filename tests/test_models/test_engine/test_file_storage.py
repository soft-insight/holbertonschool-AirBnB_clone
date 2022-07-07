#!/usr/bin/python3
"""
Test for FileStorage Class
"""
import unittest
import pep8
import os

from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage

from datetime import datetime


class TestStringMethods(unittest.TestCase):
    """
    Testing class
    """

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Adrian"
        cls.user.last_name = "Hernandez"
        cls.user.email = "1214@holbertonschool.com"
        cls.storage = FileStorage()

    def test_all(self):
        """ Tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

if __name__ == '__main__':
    unittest.main()
