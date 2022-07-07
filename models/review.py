#!/usr/bin/python3
""" This is the review class. """

from models.base_model import BaseModel


class Review(BaseModel):
    """ This class for defining Review object
    Attributes:
        place_id: place id
        user_id: user id
        text: description in string
    """
    place_id = ""
    user_id = ""
    text = ""
