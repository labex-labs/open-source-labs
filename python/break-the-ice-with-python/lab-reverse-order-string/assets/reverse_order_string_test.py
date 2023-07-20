import unittest
import sys
# Add the path to the project directory
sys.path.append("/home/labex/project")
from io import StringIO
from reverse_order_string import reverse_order_string


class TestReverseOrderString(unittest.TestCase):
    def test_reverse_order_string(self):
        # Redirect stdin and stdout to buffers
        captured_input = StringIO("hello world\n")
        captured_output = StringIO()
        sys.stdin = captured_input
        sys.stdout = captured_output

        # Call the function to reverse a string
        reverse_order_string()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "dlrow olleh"
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
