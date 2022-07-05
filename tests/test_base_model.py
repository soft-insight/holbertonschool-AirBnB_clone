#!/usr/bin/python3
""" Test of the BaseModel class """


import unittest
from models.base_model import BaseModel


class Test_BaseModel(unittest.TestCase):
    """ Test of BaseModel class 
        Attributes:
                    - id
                    - create_at
                    - updated_at
        Methods:
                    - str
                    - save
                    - to_dict
    """


if __name__ == '__main__':
    unittest.main()


