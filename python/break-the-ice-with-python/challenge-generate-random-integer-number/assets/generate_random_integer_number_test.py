import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from generate_random_integer_number import generate_random_integer_number


class TestRandomIntegerNumber(unittest.TestCase):
    def test_generate_random_integer_number(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a random integer and print it
        generate_random_integer_number()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid integer between 7 and 15
        try:
            output_int = int(output)
            self.assertIsInstance(output_int, int)
            self.assertGreaterEqual(output_int, 7)
            self.assertLessEqual(output_int, 15)
        except ValueError:
            self.fail("Output is not a valid integer")


if __name__ == "__main__":
    unittest.main()
