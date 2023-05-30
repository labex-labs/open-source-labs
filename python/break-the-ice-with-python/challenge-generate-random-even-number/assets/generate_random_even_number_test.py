import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from generate_random_even_number import generate_random_even_number


class TestRandomEvenNumber(unittest.TestCase):
    def test_random_even_number(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a random even number and print it
        generate_random_even_number()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid even integer between 0 and 10
        try:
            output_int = int(output)
            self.assertEqual(output_int % 2, 0)
            self.assertGreaterEqual(output_int, 0)
            self.assertLessEqual(output_int, 10)
        except ValueError:
            self.fail("Output is not a valid integer")


if __name__ == "__main__":
    unittest.main()
