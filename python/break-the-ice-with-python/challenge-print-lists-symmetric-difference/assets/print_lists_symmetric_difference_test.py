import unittest
import sys

sys.path.append("/home/labex/project")
from io import StringIO
from print_lists_symmetric_difference import print_lists_symmetric_difference


class TestPrintListsSymmetricDifference(unittest.TestCase):
    def test_print_lists_symmetric_difference(self):
        # Set up the input data
        input_data = "4\n2 4 5 9\n4\n2 4 11 12\n"
        sys.stdin = StringIO(input_data)

        # Call the function to print the symmetric difference of two lists
        captured_output = StringIO()
        sys.stdout = captured_output
        print_lists_symmetric_difference()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "5\n9\n11\n12"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
