import unittest
import sys

sys.path.append("/home/labex/project")

from print_the_last_5_elements import print_the_last_5_elements


class TestPrintTheLast5Elements(unittest.TestCase):
    def test_print_last_5_elements(self):
        # Redirect stdout to a buffer
        from io import StringIO
        import sys

        buffer = StringIO()
        sys.stdout = buffer

        # Call the function
        print_the_last_5_elements()

        # Get the output from the buffer
        output = buffer.getvalue().strip()

        # Assert that the output is correct
        expected_output = str([i**2 for i in range(16, 21)])
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
