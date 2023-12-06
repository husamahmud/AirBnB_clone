#!/usr/bin/python3
"""Module for FileStorage class"""

import json
import os


class FileStorage:
    """FileStorage Class"""
    __file_path = "file.json"
    __objects = {}

    @classmethod
    def all(cls):
        """Returns all objects stored in __objects"""
        return cls.__objects

    @classmethod
    def new(cls, obj):
        """Adds a new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        cls.__objects[key] = obj

    @classmethod
    def save(cls):
        """Serializes __objects to the JSON file"""
        my_dict = {key: val.to_dict() for key, val in cls.__objects.items()}
        with open(cls.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r") as f:
                my_dict = json.load(f)
                for key, val in my_dict.items():
                    self.__objects[key] = eval(val['__class__'])(**val)
