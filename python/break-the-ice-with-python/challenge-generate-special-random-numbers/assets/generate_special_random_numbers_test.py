import unittest
from io import StringIO
import sys
sys.path.append("/home/labex/project")
from generate_special_random_numbers import generate_special_random_numbers

class TestSpecialRandomNumbers(unittest.TestCase):
    def test_special_random_numbers(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a special random number and print it
        generate_special_random_numbers()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid integer that is divisible by 35 and between 10 and 150
        try:
            output_int = int(output)
            self.assertEqual(output_int % 35, 0)
            self.assertGreaterEqual(output_int, 10)
            self.assertLessEqual(output_int, 150)
        except ValueError:
            self.fail("Output is not a valid integer")

if __name__ == '__main__':
    unittest.main()
