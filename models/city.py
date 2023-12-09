#!/usr/bin/python3
"""Module for City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """City Class"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new City instance."""
        super().__init__(*args, **kwargs)
