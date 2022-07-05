#!/usr/bin/python3
""" A class that serializes instances to JSON files
    and deserializes JSON files to instances.
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """ Private attributes:
            __file_path
            __objects
        Public methods:
            all(self)
            new(self, obj)
            save(self)
            reload(self)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects.update({key: obj})

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """
        obj_dict = {}
        for k, v in self.__objects.items():
            obj_dict.update({k, v.to_dict})

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(obj_dict, f)

    def reload(self):
        """ deserializes the JSON file to __objects """
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                json_string = json.load(f)
        except Exception:
            pass

