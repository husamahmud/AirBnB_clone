#!/usr/bin/python3
"""Module for BaseModel class"""
from uuid import uuid4
from datetime import datetime

import models


class BaseModel:
    """BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    setattr(self, key,
                            datetime.strptime(val, "%Y-%m-%d %H:%M:%S.%f"))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the BaseModel."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        return {
            'id': self.id,
            '__class__': self.__class__.__name__,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
