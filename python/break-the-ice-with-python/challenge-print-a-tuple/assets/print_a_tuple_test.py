import unittest
import sys

sys.path.append("/home/labex/project")

from print_a_tuple import print_a_tuple


class TestPrintATuple(unittest.TestCase):
    def test_print_a_tuple(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys

        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        print_a_tuple()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = str(tuple([i**2 for i in range(1, 21)]))
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
