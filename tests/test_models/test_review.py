#!/usr/bin/python3

"""
    This func defines the classes of Review.
"""


from models.review import Review
import unittest
import models
import os


class TestReview(unittest.TestCase):
    """Representings a Review."""

    def setUp(self):
        """Settings Up method"""

        self.review = Review()

    def TearDown(self):
        """Tearings Down method."""

        del self.review

    def test_docstring(self):
        """Testingss docstring for the module and the class"""

        self.assertIsNotNone(
            models.review.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Review.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testingss File review.py permissions"""

        test_file = os.access("models/review.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/review.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/review.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testingss type object of Review"""

        self.assertEqual(
            str(type(self.review)),
            "<class 'models.review.Review'>")
        self.assertIsInstance(self.review, Review)
