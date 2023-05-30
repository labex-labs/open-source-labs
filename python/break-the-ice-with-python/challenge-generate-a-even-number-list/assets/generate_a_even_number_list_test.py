import unittest
from io import StringIO
import sys
sys.path.append("/home/labex/project")
from generate_a_even_number_list import generate_a_even_number_list

class TestEvenNumberList(unittest.TestCase):
    def test_generate_a_even_number_list(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a list of even numbers and print it
        generate_a_even_number_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of 5 even integers between 100 and 200
        try:
            output_list = eval(output)
            self.assertIsInstance(output_list, list)
            self.assertEqual(len(output_list), 5)
            for num in output_list:
                self.assertIsInstance(num, int)
                self.assertGreaterEqual(num, 100)
                self.assertLessEqual(num, 200)
                self.assertEqual(num % 2, 0)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of even integers")

if __name__ == '__main__':
    unittest.main()
