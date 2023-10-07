import unittest
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from word_counting import word_counting


class TestWordCounting(unittest.TestCase):
    def test_word_counting(self):
        # Set up the input data
        input_data = "6\napple\nbanana\napple\nbanana\norange\nbanana\n"
        sys.stdin = StringIO(input_data)

        # Call the function to count the words
        captured_output = StringIO()
        sys.stdout = captured_output
        word_counting()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "3\n2 3 1"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
