import unittest
import sys

sys.path.append("/home/labex/project")

from print_half_of_a_tuple import print_half_of_a_tuple

class TestPrintHalfOfATuple(unittest.TestCase):
    def test_print_half_of_a_tuple(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys
        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        print_half_of_a_tuple()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = "1 2 3 4 5 \n6 7 8 9 10"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
