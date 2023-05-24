import unittest
import re
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from remove_special_numbers_from_list import remove_special_numbers_from_list


class TestRemoveSpecialNumbers(unittest.TestCase):
    def test_remove_special_numbers(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to remove special numbers
        remove_special_numbers_from_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of numbers
        try:
            numbers = re.findall(r"\d+", output)
            if len(numbers) == 0:
                self.fail("Output is empty")
            for number in numbers:
                self.assertTrue(int(number) % 35 != 0)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of numbers")


if __name__ == "__main__":
    unittest.main()
