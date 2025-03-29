"""Basic tests for the ucl package."""

import unittest


class TestBasic(unittest.TestCase):
    def test_import(self):
        """Test that the package can be imported."""
        import ucl

        self.assertIsNotNone(ucl)

    def test_version(self):
        """Test that the version is available and is a string."""
        import ucl

        self.assertIsNotNone(ucl.__version__)
        self.assertIsInstance(ucl.__version__, str)
