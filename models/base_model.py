#!/usr/bin/python3
""" Module name: base_model.
    Class BaseModel - This class defines all common
    attributes/methods for other classes.
"""
import uuid
import models
from datetime import datetime


class BaseModel:
    """ BaseModel -
        Public Instances:
        id: instance of type string, assigned with uuid
        created_at: instance of type datetime
                    assigns a datetime at the moment of creation
        updated_at: datetime - assign with the current datetime
                    when an instance is created and it will be
                    updated
    """

    def __init__(self, *args, **kwargs):
        """ The constructor of the class BaseModel
            with attributes:
            id
            created_at
            updated_at
        """
        fmtDate = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for i in kwargs.keys():
                if i == 'created_at' or i == 'updated_at':
                    kwargs[i] = datetime.strptime(kwargs[i], fmtDate)
                    setattr(self, i, kwargs[i])
                if i != '__class__':
                    setattr(self, i, kwargs[i])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Method that represents the class as string """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """ Method that saves the updates """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ Method that returns a dictionary
            containing all keys/values of __dict__ of the instance.
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        base_dict["created_at"] = self.created_at.isoformat()
        base_dict["updated_at"] = self.updated_at.isoformat()
        return base_dict
