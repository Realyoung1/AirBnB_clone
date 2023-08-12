#!/usr/bin/python3

"""
    This func defines the classes of TestPlace.
"""


from models.place import Place
import unittest
import models
import os


class TestPlace(unittest.TestCase):
    """Representings the Place."""

    def setUp(self):
        """Settings Up method"""

        self.place = Place()

    def TearDown(self):
        """Tearingss Down method."""

        del self.place

    def test_docstring(self):
        """Testingss docstring for the module and the class"""

        self.assertIsNotNone(
            models.place.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Place.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testingss File place.py permissions"""

        test_file = os.access("models/place.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/place.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/place.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testingss type object of Place"""

        self.assertEqual(
            str(type(self.place)),
            "<class 'models.place.Place'>")
        self.assertIsInstance(self.place, Place)
