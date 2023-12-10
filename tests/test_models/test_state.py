#!/usr/bin/python3
"""Unittest for State model"""

import unittest

from models.state import State


class Test_State_model(unittest.TestCase):
    """test class for the State model."""

    def test_default_values(self):
        """test a default values for the state model"""
        state = State()
        self.assertEqual(state.name, "")
