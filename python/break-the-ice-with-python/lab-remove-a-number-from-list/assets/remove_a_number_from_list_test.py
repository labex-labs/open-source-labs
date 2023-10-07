import unittest
import re
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from remove_a_number_from_list import remove_a_number_from_list


class TestRemoveANumber(unittest.TestCase):
    def test_remove_a_number(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to remove a number
        remove_a_number_from_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of numbers
        try:
            numbers = list(map(int, re.findall(r"\d+", output)))
            expected = [12, 35, 88, 120, 155]
            self.assertListEqual(numbers, expected)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of numbers")


if __name__ == "__main__":
    unittest.main()
