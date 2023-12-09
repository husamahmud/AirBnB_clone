#!/usr/bin/python3
"""Unittest for base model"""
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    test class for the max_integer() function.
    """
    b = BaseModel()
    b.name = "My First Model"
    b.my_number = 89

    def test_save(self):
        """"
            test save class method
        """
        before_update_time = self.b.updated_at
        self.b.my_number = 90
        self.b.save()
        after_update_time = self.b.updated_at
        self.assertNotEqual(before_update_time, after_update_time)
        all_objects = storage.all()
        obj = all_objects[f"{self.b.__class__.__name__}.{self.b.id}"]
        new_number = obj.my_number
        self.assertEqual(new_number, 90)

    def test_create_instance_without_kwargs(self):
        """
        create an instance of class without kwargs
        """
        self.assertIsInstance(self.b, BaseModel)
        self.assertIsInstance(self.b.id, str)
        self.assertIsInstance(self.b.created_at, datetime)
        self.assertIsInstance(self.b.updated_at, datetime)
        self.assertEqual(self.b.name, "My First Model")
        self.assertEqual(self.b.my_number, 89)

    def test_create_instance_with_kwargs(self):
        """
        create an instance of class using kwargs
        """
        my_base_json = self.b.to_dict()
        new_b = BaseModel(**my_base_json)
        self.assertIsInstance(new_b, BaseModel)
        self.assertIsInstance(new_b.id, str)
        self.assertIsInstance(new_b.created_at, datetime)
        self.assertIsInstance(new_b.updated_at, datetime)
        self.assertEqual(new_b.name, "My First Model")
        self.assertEqual(new_b.my_number, 89)
        self.assertNotEqual(new_b, self.b)
        self.assertDictEqual(new_b.__dict__, self.b.__dict__)

    def test_str(self):
        """
            test str method

            check for string representaion
        """
        s = f"[{self.b.__class__.__name__}] ({self.b.id}) {self.b.__dict__}"
        self.assertEqual(self.b.__str__(), s)

    def test_to_dict(self):
        """
            test to_dict class method
        """
        to_dict_returned_dict = self.b.to_dict()
        expected_dic = self.b.__dict__.copy()
        expected_dic["__class__"] = self.b.__class__.__name__
        expected_dic["updated_at"] = self.b.updated_at.isoformat()
        expected_dic["created_at"] = self.b.created_at.isoformat()
        self.assertDictEqual(expected_dic, to_dict_returned_dict)
