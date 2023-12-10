#!/usr/bin/python3
"""Module for Base unit tests."""

import unittest
import datetime
import os

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel(unittest.TestCase):
    """Tests the Base class."""

    def setUp(self):
        """Imports module, instantiates class"""
        self.base_model = BaseModel()

    def tearDown(self):
        """Cleans up resources after tests"""
        del self.base_model
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_initialization(self):
        """Ensure that the init is correct"""
        self.assertEqual(str(type(self.base_model)),
                         "<class 'models.base_model.BaseModel'>")
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    def test_str_representation(self):
        """Ensure that the string representation is right"""
        str_repr = str(self.base_model)
        self.assertIn(self.base_model.__class__.__name__, str_repr)
        self.assertIn(self.base_model.id, str_repr)

    def test_save_method(self):
        """Ensure that the save mthd updates the updated_at attribute"""
        initial_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(initial_updated_at, self.base_model.updated_at)

    def test_to_dict_method(self):
        """Ensure that the to_dict mthd returns a dict with expected keys"""
        model_dict = self.base_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('__class__', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_to_dict_timestamp_format(self):
        """Ensure that timestamp in the to_dict mthd in the correct format"""
        model_dict = self.base_model.to_dict()
        created_at = datetime.datetime \
            .strptime(model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        created_at = datetime
        updated_at = datetime.datetime \
            .strptime(model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')

    def test_init_from_dict(self):
        """Ensure that an instance can be created from a dict"""
        original_model = BaseModel()
        model_dict = original_model.to_dict()
        new_model = BaseModel(**model_dict)
        t1 = original_model.to_dict()
        t2 = new_model.to_dict()
        self.assertEqual(t1, t2)

    def test_init_from_dict_with_args(self):
        """Ensure that *args is not used when creating an inst from a dict"""
        original_model = BaseModel()
        model_dict = original_model.to_dict()
        new_model = BaseModel("arg1", "arg2", **model_dict)
        self.assertEqual(original_model.to_dict(), new_model.to_dict())

    def test_init_from_dict_with_datetime_strings(self):
        """datetime strs are correctly converted to datetime objs"""
        model_dict = {
            'id': '123',
            'created_at': '2022-01-01T12:34:56.789',
            'updated_at': '2022-01-01T12:34:56.789',
            '__class__': 'BaseModel'
        }
        new_model = BaseModel(**model_dict)
        self.assertIsInstance(new_model.created_at, datetime.datetime)
        self.assertIsInstance(new_model.updated_at, datetime.datetime)

    def test_save_and_reload_instance(self):
        """Ensure that an inst can be saved and reloaded"""
        original_model = BaseModel()
        model_id = original_model.id
        storage.save()
        storage.reload()
        reloaded_model = storage.all().get(f"BaseModel.{model_id}")
        self.assertIsNotNone(reloaded_model)
        self.assertEqual(original_model.to_dict(), reloaded_model.to_dict())

    def test_save_and_reload_multiple_instances(self):
        """Ensure that multiple insts can be saved and reloaded"""
        original_model1 = BaseModel()
        original_model2 = BaseModel()
        model_id1, model_id2 = original_model1.id, original_model2.id
        storage.save()
        storage.reload()
        reloaded_models = storage.all()
        self.assertIn(f"BaseModel.{model_id1}", reloaded_models)
        self.assertIn(f"BaseModel.{model_id2}", reloaded_models)
        self.assertEqual(original_model1.to_dict(),
                         reloaded_models[f"BaseModel.{model_id1}"].to_dict())
        self.assertEqual(original_model2.to_dict(),
                         reloaded_models[f"BaseModel.{model_id2}"].to_dict())


if __name__ == '__main__':
    unittest.main()
