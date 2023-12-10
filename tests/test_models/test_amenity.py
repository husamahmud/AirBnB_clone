#!/usr/bin/python3
"""Unittest for Amenity model"""

import unittest

from models.amenity import Amenity


class Test_Amenity_model(unittest.TestCase):
    """test class for the Amenity model."""

    def test_default_values(self):
        """test the default values for the Amenity model"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
