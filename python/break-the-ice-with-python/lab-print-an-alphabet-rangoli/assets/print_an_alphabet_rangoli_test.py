import unittest
import sys
sys.path.append("/home/labex/project")
from io import StringIO
from print_an_alphabet_rangoli import rangoli


class TestRangoli(unittest.TestCase):
    def test_rangoli(self):
        # Set up the input data
        input_data = "5\n"
        sys.stdin = StringIO(input_data)

        # Call the function to generate the rangoli pattern
        captured_output = StringIO()
        sys.stdout = captured_output
        rangoli(5)

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "--------e--------\n------e-d-e------\n----e-d-c-d-e----\n--e-d-c-b-c-d-e--\ne-d-c-b-a-b-c-d-e\n--e-d-c-b-c-d-e--\n----e-d-c-d-e----\n------e-d-e------\n--------e--------"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
