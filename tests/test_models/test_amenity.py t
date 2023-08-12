#!/usr/bin/python3

"""
    This func defines the classes of Amenity.
"""


from models.amenity import Amenity
import unittest
import models
import os


class TestAmenity(unittest.TestCase):
    """Representingss the Amenity."""

    def setUp(self):
        """Setting up method"""

        self.amenity = Amenity()

    def TearDown(self):
        """Tearing Down method."""

        del self.amenity

    def test_docstring(self):
        """Testing docstring for the modules and the classes"""

        self.assertIsNotNone(
            models.amenity.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(Amenity.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testings Files amenity.py permissions"""

        test_file = os.access("models/amenity.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/amenity.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/amenity.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testings types objects of Amenity"""

        self.assertEqual(
            str(type(self.amenity)),
            "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(self.amenity, Amenity)
