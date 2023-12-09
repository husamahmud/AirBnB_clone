#!/usr/bin/python3
"""Module for State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """State Class"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes a new State instance."""
        super().__init__(*args, **kwargs)
