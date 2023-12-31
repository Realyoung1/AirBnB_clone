#!/usr/bin/python3

"""
   This func defines the classes of City.
"""


from models.city import City
import unittest
import models
import os


class TestCity(unittest.TestCase):
    """Representingss the  City."""

    def setUp(self):
        """Setting up method"""

        self.city = City()

    def TearDown(self):
        """Tearing Down method."""

        del self.city

    def test_docstring(self):
        """Testingss docstring for the module and the class"""

        self.assertIsNotNone(
            models.city.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(City.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testingss File city.py permissions"""

        test_file = os.access("models/city.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/city.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/city.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testingss type object of City"""

        self.assertEqual(
            str(type(self.city)),
            "<class 'models.city.City'>")
        self.assertIsInstance(self.city, City)
