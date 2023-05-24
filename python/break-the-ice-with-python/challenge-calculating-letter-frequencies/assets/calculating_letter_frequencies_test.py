import unittest
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from calculating_letter_frequencies import calculating_letter_frequencies


class TestCalculatingLetterFrequencies(unittest.TestCase):
    def test_calculating_letter_frequencies(self):
        # Set up the input data
        input_data = "hello\n"
        sys.stdin = StringIO(input_data)

        # Call the function to calculate the letter frequencies
        captured_output = StringIO()
        sys.stdout = captured_output
        calculating_letter_frequencies()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "l 2\ne 1\nh 1\no 1"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
