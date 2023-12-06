#!/usr/bin/python3
"""Module for BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self):
        """Initializes a new instance of the BaseModel class."""
        self.id = str(uuid4())
        self.my_number = None
        self.name = None
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Save the current state of the BaseModel."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        return {
            'id': self.id,
            'my_number': self.my_number,
            'name': self.name,
            '__class__': 'BaseModel',
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
