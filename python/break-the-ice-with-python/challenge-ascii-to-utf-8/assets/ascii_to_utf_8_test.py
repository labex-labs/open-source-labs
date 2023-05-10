from unittest.mock import patch
import unittest
import sys

sys.path.append("/home/labex/project")

from ascii_to_utf_8 import ascii_to_utf_8

class TestGetEmailUsername(unittest.TestCase):
    def test_get_email_username(self):
        # Simulate user input
        user_input = "python"
        expected_output = b'python'

        # Redirect standard input to simulate user input
        with patch('builtins.input', return_value=user_input):
            # Call the function and check the output
            self.assertEqual(ascii_to_utf_8(), expected_output)

if __name__ == '__main__':
    unittest.main()
