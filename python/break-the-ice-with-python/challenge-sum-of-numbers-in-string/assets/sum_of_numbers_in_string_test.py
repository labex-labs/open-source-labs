import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from sum_of_numbers_in_string import sum_of_numbers_in_string


class TestPrintValue(unittest.TestCase):
    def test_print(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        sum_of_numbers_in_string("123", "456")
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue().strip(), "579")


if __name__ == "__main__":
    unittest.main()
