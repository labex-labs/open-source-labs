import unittest
import sys
# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from permutation_of_lists import permuation_generator

class TestPermutationGenerator(unittest.TestCase):
    def test_permutation_generator(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate permutations
        x = [1, 2, 3]
        permuation_generator(x)

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "(1, 2, 3)\n(1, 3, 2)\n(2, 1, 3)\n(2, 3, 1)\n(3, 1, 2)\n(3, 2, 1)"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
