import unittest
import sys

# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from counting_characters_in_strings import counting_characters_in_strings


class TestCountingCharactersInStrings(unittest.TestCase):
    def test_counting_characters_in_strings(self):
        # Redirect stdin and stdout to buffers
        captured_input = StringIO("hello world\n")
        captured_output = StringIO()
        sys.stdin = captured_input
        sys.stdout = captured_output

        # Call the function to count characters in a string
        counting_characters_in_strings()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "d,1\ne,1\nh,1\nl,3\no,2\nr,1\nw,1"
        self.assertEqual(output, expected_output)


if __name__ == "__main__":
    unittest.main()
