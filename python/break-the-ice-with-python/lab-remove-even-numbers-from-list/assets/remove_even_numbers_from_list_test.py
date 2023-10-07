import unittest
import re
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from remove_even_numbers_from_list import remove_even_numbers_from_list


class TestRemoveEvenNumbers(unittest.TestCase):
    def test_remove_even_numbers(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to remove even numbers
        remove_even_numbers_from_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of odd numbers
        try:
            odd_numbers = re.findall(r"\d+", output)
            print(odd_numbers)
            for number in odd_numbers:
                self.assertTrue(int(number) % 2 != 0)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of odd numbers")


if __name__ == "__main__":
    unittest.main()
