import unittest
import sys

# Add the path to the project directory
sys.path.append("/home/labex/project")
import re
from io import StringIO
from remove_duplicate_numbers_from_list import remove_duplicate_numbers_from_list


class TestRemoveDuplicatesFromList(unittest.TestCase):
    def test_remove_duplicates_from_list(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to remove duplicate numbers from a list
        remove_duplicate_numbers_from_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that each number in the output is in the expected list
        try:
            numbers = list(map(int, re.findall(r"\d+", output)))
            expected = [12, 24, 35, 88, 120, 155]
            for number in numbers:
                self.assertIn(number, expected)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of numbers")


if __name__ == "__main__":
    unittest.main()
