import unittest
import sys
import math
from io import StringIO

# Add the path of the code file
sys.path.append("/home/labex/project")

# Import the code to be tested
from compute_the_distance import compute_the_distance


class TestYour(unittest.TestCase):
    def test_output(self):
        # Redirect standard input and output to buffer
        stdin = sys.stdin
        stdout = sys.stdout
        sys.stdin = StringIO()
        sys.stdout = StringIO()

        # Input test data
        test_input = "UP 5\nDOWN 3\nLEFT 3\nRIGHT 2\n\n"
        sys.stdin.write(test_input)
        sys.stdin.seek(0)

        # Run the code
        compute_the_distance()

        # Restore standard input and output
        output = sys.stdout.getvalue()
        sys.stdin = stdin
        sys.stdout = stdout

        # Check if the output matches the expected result
        expected_output = "2\n"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
