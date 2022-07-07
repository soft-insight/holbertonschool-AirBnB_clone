#!/usr/bin/python3
""" This module represent the User definition. """

from models.base_model import BaseModel


class User(BaseModel):
    """ This class define the user object
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
