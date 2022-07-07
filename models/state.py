#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """ This is the class for defining State
    Attributes:
        name: input name
    """
    name = ""
