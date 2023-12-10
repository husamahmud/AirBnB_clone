#!/usr/bin/python3
"""Unittest for City model"""

import unittest

from models.city import City


class Test_City_model(unittest.TestCase):
    """test class for the city modle."""

    def test_default_values(self):
        """test the default value for the city model"""
        city = City()
        self.assertEqual(city.name, "")
        self.assertEqual(city.state_id, "")
