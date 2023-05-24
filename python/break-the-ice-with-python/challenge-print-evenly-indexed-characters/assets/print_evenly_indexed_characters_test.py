import unittest
import sys

# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from print_evenly_indexed_characters import print_evenly_indexed_characters


class TestPrintEvenlyIndexedCharacters(unittest.TestCase):
    def test_print_evenly_indexed_characters(self):
        # Redirect stdout to a buffer
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function to print evenly indexed characters
        print_evenly_indexed_characters()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "Helloworld"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
