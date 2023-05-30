import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from calculating_number_of_digits_and_letters import (
    calculating_number_of_digits_and_letters,
)


class TestCalculatingNumberOfDigitsAndLetters(unittest.TestCase):
    def test_calculating_number_of_digits_and_letters(self):
        # Set up the input data
        input_data = "Hello123\n"
        sys.stdin = StringIO(input_data)

        # Call the function to calculate the number of digits and letters
        captured_output = StringIO()
        sys.stdout = captured_output
        calculating_number_of_digits_and_letters()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "Digit - 3\nLetter - 5"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
