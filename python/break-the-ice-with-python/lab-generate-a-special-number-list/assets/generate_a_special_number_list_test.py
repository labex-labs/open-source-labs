import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from generate_a_special_number_list import generate_a_special_number_list


class TestSpecialNumberList(unittest.TestCase):
    def test_generate_a_special_number_list(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to generate a list of special numbers and print it
        generate_a_special_number_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of 5 integers that are divisible by 35 and between 1 and 1000
        try:
            output_list = eval(output)
            self.assertIsInstance(output_list, list)
            self.assertEqual(len(output_list), 5)
            for num in output_list:
                self.assertIsInstance(num, int)
                self.assertGreaterEqual(num, 1)
                self.assertLessEqual(num, 1000)
                self.assertEqual(num % 35, 0)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of special integers")


if __name__ == "__main__":
    unittest.main()
