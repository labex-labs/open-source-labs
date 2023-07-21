import unittest
from io import StringIO
import sys
sys.path.append("/home/labex/project")
from generate_random_float import generate_random_float

class TestRandomNumber(unittest.TestCase):
    def test_random_number(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a random number and print it
        generate_random_float()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid float between 10 and 100
        try:
            output_float = float(output)
            self.assertGreaterEqual(output_float, 10)
            self.assertLessEqual(output_float, 100)
        except ValueError:
            self.fail("Output is not a valid float")

if __name__ == '__main__':
    unittest.main()
