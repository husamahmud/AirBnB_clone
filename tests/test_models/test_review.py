#!/usr/bin/python3
"""Unittest for Review model"""

import unittest

from models.review import Review


class Test_Review_model(unittest.TestCase):
    """test class for the Review model."""

    def test_default_values(self):
        """test the default values for the Review model"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
