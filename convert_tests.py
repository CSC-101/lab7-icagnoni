import convert
import unittest

class TestStrToFloat(unittest.TestCase):
    # Task 1

    def test_str_to_float(self):
        self.assertEqual(convert.str_to_float("10"), 10)

    def test_invalid_string(self):
        self.assertIsNone(convert.str_to_float("abc"))
