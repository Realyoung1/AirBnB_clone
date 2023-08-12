#!/usr/bin/python3

"""
    This func defines the classes of TestFileStorage.
"""


from models.engine.file_storage import FileStorage
import unittest
import models
import os


class TestFileStorage(unittest.TestCase):
    """Representingss the  TestFileStorage."""

    def setUp(self):
        """Setting Up method"""

        self.file_storage = FileStorage()

    def TearDown(self):
        """Tearing Down method."""

        del self.file_storage

    def test_docstring(self):
        """Testings docstring for the modules and the classes"""

        self.assertIsNotNone(
            models.engine.file_storage.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(FileStorage.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testing Files file_storage.py permissions"""

        test_file = os.access("models/engine/file_storage.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/engine/file_storage.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/engine/file_storage.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testing type objects of FileStorage"""

        self.assertEqual(
            str(type(self.file_storage)),
            "<class 'models.engine.file_storage.FileStorage'>")
        self.assertIsInstance(self.file_storage, FileStorage)
