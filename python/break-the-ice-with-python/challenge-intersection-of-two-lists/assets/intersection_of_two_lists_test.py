import unittest
import re
import sys

# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from intersection_of_two_lists import intersection_of_two_lists


class TestIntersectionOfLists(unittest.TestCase):
    def test_intersection_of_lists(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to find the intersection of two lists
        intersection_of_two_lists()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of numbers
        try:
            numbers = list(map(int, re.findall(r"\d+", output)))
            expected = [35]
            self.assertListEqual(numbers, expected)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of numbers")


if __name__ == "__main__":
    # Add the path to the project directory
    sys.path.append("/home/labex/project")
    unittest.main()
