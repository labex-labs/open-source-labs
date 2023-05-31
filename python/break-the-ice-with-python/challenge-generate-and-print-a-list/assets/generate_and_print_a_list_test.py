import unittest
import sys

sys.path.append("/home/labex/project")

from generate_and_print_a_list import generate_and_print_a_list

class TestPrintList(unittest.TestCase):
    def test_print_list(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys
        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        generate_and_print_a_list()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = str([i ** 2 for i in range(1, 21)])
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
