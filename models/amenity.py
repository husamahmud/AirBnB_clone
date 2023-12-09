#!/usr/bin/python3
"""Module for Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Amenity instance."""
        super().__init__(*args, **kwargs)
