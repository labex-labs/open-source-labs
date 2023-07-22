import unittest
import sys
sys.path.append("/home/labex/project")
from io import StringIO
from wrap_string_into_paragraph import wrap_string_into_paragraph

class TestWrapStringIntoParagraph(unittest.TestCase):
    def test_wrap_string_into_paragraph(self):
        # Set up the input data
        input_data = "Hello world! This is a long string that needs to be wrapped into multiple lines.\n10\n"
        sys.stdin = StringIO(input_data)

        # Call the function to wrap the string into paragraphs
        captured_output = StringIO()
        sys.stdout = captured_output
        wrap_string_into_paragraph()

        # Get the printed output from the buffer
        output = captured_output.getvalue().strip()

        # Check that the output is correct
        expected_output = "Hello\nworld!\nThis is a\nlong\nstring\nthat needs\nto be\nwrapped\ninto\nmultiple\nlines."
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    unittest.main()
