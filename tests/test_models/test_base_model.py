#!/usr/bin/python3
""" Unittests for BaseModel """
import unittest
from datetime import datetime
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Tests for BaseModel """

    def test_instance(self):
        """ Test instances created by BaseModel """
        my_model = BaseModel()

        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

    def test_newInstances(self):
        """ Test new instances created """
        my_model = BaseModel()
        my_model.number = 89
        my_model.name = "aa"

        self.assertTrue(hasattr(my_model, 'number'))
        self.assertTrue(hasattr(my_model, 'name'))
        self.assertTrue(my_model.number, 89)
        self.assertTrue(my_model.name, 'aa')

    def test_types(self):
        """ Test types of the objects """
        model2 = BaseModel()
        self.assertEqual(type(model2.id), str)
        self.assertEqual(type(model2.created_at), datetime)
        self.assertEqual(type(model2.updated_at), datetime)


if __name__ == "__main__":
    unittest.main()
