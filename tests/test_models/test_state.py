#!/usr/bin/python3

"""
   This func defines the classes of TestState.
"""


from models.state import State
import unittest
import models
import os


class TestState(unittest.TestCase):
    """Representingss the State."""

    def setUp(self):
        """Settings Up method"""

        self.state = State()

    def TearDown(self):
        """Tearings Down method."""

        del self.state

    def test_docstring(self):
        """Testings docstring for the module and the class"""

        self.assertIsNotNone(
            models.state.__doc__,
            "No docstring in the module"
        )
        self.assertIsNotNone(State.__doc__, "No docstring in the class")

    def test_permissions_file(self):
        """Testings File state.py permissions"""

        test_file = os.access("models/state.py", os.R_OK)
        self.assertTrue(test_file, "Read permissions")
        test_file = os.access("models/state.py", os.W_OK)
        self.assertTrue(test_file, "Write Permissions")
        test_file = os.access("models/state.py", os.X_OK)
        self.assertTrue(test_file, "Execute permissions")

    def test_type_object(self):
        """Testings type object of State"""

        self.assertEqual(
            str(type(self.state)),
            "<class 'models.state.State'>")
        self.assertIsInstance(self.state, State)
