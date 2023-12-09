#!/usr/bin/python3
"""Module for Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new Review instance."""
        super().__init__(*args, **kwargs)
