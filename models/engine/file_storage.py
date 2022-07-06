#!/usr/bin/python3
""" This Class define FileStorage:
        it completes the correct
        serialization/deserialization process
"""

from models.base_model import BaseModel
import json
import os


class FileStorage:
    """ Class FileStorage
        Private class attributes:
            __file_path: string - path to the JSON file (ex: file.json)
            __objects: dictionary - empty but will store all objects
                by <class name>.id (ex: to store a BaseModel object
                with id=12121212, the key will be BaseModel.12121212)
        Public instance methods:
            all(self): returns the dictionary __objects
            new(self, obj): sets in __objects the
                    obj with key <obj class name>.id
            save(self): serializes __objects to the
                    JSON file (path: __file_path)
            reload(self): deserializes the JSON file
                    to __objects (only if the JSON file
                    (__file_path) exists ; otherwise, do nothing.
                    If the file doesn’t exist, no exception should be raised)
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ Sets in __objects the
            obj with key <obj class name>.id
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file (path: __file_path) """
        base_dict = {}
        for k, v in self.__objects.items():
            base_dict[k] = v.to_dict()

        with open(self.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(base_dict, f)

    def reload(self):
        """Deserializes __file_path to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as f:
                base_dict = json.load(f)
                for k, v in base_dict.items():
                    self.__objects[k] = eval(v['__class__'])(**v)
        except Exception:
            pass
