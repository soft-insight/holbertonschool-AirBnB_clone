#!/usr/bin/python3
""" This is the city class. """

from models.base_model import BaseModel


class City(BaseModel):
    """This class for defining City object
        Attributes:
        state_id: state id
        name: input name
    """
    state_id = ""
    name = ""
