import unittest
from io import StringIO
import sys

sys.path.append("/home/labex/project")
from shuffle_and_print_the_list import shuffle_and_print_the_list


class TestShuffleList(unittest.TestCase):
    def test_shuffle_list(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to shuffle a list and print it
        shuffle_and_print_the_list()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is a valid list of 4 integers
        try:
            output_list = eval(output)
            self.assertIsInstance(output_list, list)
            self.assertEqual(len(output_list), 4)
            for num in output_list:
                self.assertIsInstance(num, int)
            # Check that the output list contains the same elements as the expected list
            lst = [3, 6, 7, 8]
            self.assertCountEqual(lst, output_list)
        except (ValueError, TypeError):
            self.fail("Output is not a valid list of integers")


if __name__ == "__main__":
    unittest.main()
