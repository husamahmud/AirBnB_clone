#!/usr/bin/python3
"""Module for FileStorage class"""

import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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

    def delete(self, key):
        """Deletes an object from __objects using the provided key"""
        del self.__objects[key]

    @classmethod
    def save(cls):
        """Serializes __objects to the JSON file"""
        my_dict = {key: val.to_dict() for key, val in cls.__objects.items()}
        with open(cls.__file_path, 'w') as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path) as f:
                objects = json.load(f)
                for obj in objects.values():
                    cls_name = obj["__class__"]
                    del obj["__class__"]
                    self.new(eval(cls_name)(**obj))
        except FileNotFoundError:
            return
