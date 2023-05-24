import unittest
import sys

# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from the_chicken_and_rabbit_problem import solve


class TestSolve(unittest.TestCase):
    def test_solve(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to solve the problem
        numheads = 35
        numlegs = 94
        solutions = solve(numheads, numlegs)
        print(solutions)

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "(23, 12)"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
