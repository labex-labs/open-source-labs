import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from recursive_summation import rec


class TestRec(unittest.TestCase):
    def test_rec(self):
        # Set up the input data
        input_data = "5\n"
        sys.stdin = StringIO(input_data)

        # Call the function to calculate the sum
        captured_output = StringIO()
        sys.stdout = captured_output
        n = int(input())
        sum = rec(n)
        print(sum)

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "15"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
