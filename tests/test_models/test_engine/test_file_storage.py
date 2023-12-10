#!/usr/bin/python3
"""Unittest for FileStorage model
"""
import unittest
import json
import os
import unittest
from datetime import datetime
from sre_parse import State

import models
from models.city import City
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
from models.place import Place
from models.review import Review

from models.user import User


class Test_FileStorage_model(unittest.TestCase):
    """test class for the FileStorage model."""

    def test_default_values(self):
        """test the default values for the FileStorage model
        os.remove("file.json")"""
        storage = FileStorage()
        self.assertIsInstance(storage.all(), dict)
        base = BaseModel()
        base.save()
        objs = storage.all()
        obj = objs[f"{base.__class__.__name__}.{base.id}"]
        self.assertEqual(base, obj)
        self.assertIsInstance(storage, FileStorage)

        with open("file.json", "r", encoding='utf-8') as f:
            json_objs = json.load(f)
            json_obj = json_objs[f"{base.__class__.__name__}.{base.id}"]
        self.assertEqual(base.to_dict(), json_obj)
        storage.reload()
        models = {
            'User': User,
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        for key, val in json_objs.items():
            constractor = val["__class__"]
            for model, cls in models.items():
                if constractor == model:
                    self.assertEqual(str(objs[key]), str(cls(**val)))
        cls = base.to_dict()['__class__']
        self.assertEqual(str(obj), str(models[cls](**obj.to_dict())))

        """"test save class method"""
        before_update_time = base.updated_at
        base.my_number = 90
        base.save()
        after_update_time = base.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        new_number = obj.my_number
        self.assertEqual(new_number, 90)


class TestBaseModel(unittest.TestCase):
    """test class for the BaseModel model."""
    b = BaseModel()
    b.name = "My First Model"
    b.my_number = 89

    def test_create_instance_without_kwargs(self):
        """create an instance of class without kwargs"""
        self.assertIsInstance(self.b, BaseModel)
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)

    def test_create_instance_with_kwargs(self):
        """create an instance of class using kwargs"""
        my_base_json = self.b.to_dict()
        new_base = BaseModel(**my_base_json)
        self.assertIsInstance(new_base, BaseModel)
        self.assertIsInstance(new_base.id, str)
        self.assertIsInstance(new_base.created_at, datetime)
        self.assertIsInstance(new_base.updated_at, datetime)
        self.assertNotEqual(new_base, self.b)

    def test_save(self):
        """"test save class method"""
        before_update_time = self.b.updated_at
        self.b.my_number = 90
        self.b.save()
        after_update_time = self.b.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        all_objects = storage.all()
        obj = all_objects[f"{self.b.__class__.__name__}.{self.b.id}"]

    def test_str(self):
        """test str method"""
        s = f"[{self.b.__class__.__name__}] ({self.b.id}) {self.b.__dict__}"
        self.assertEqual(self.b.__str__(), s)
