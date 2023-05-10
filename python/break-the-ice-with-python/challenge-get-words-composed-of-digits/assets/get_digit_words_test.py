from unittest.mock import patch
import unittest
import sys
import re

sys.path.append("/home/labex/project")

from get_digit_words import get_digit_words

class TestGetEmailUsername(unittest.TestCase):
    def test_get_email_username(self):
        # Simulate user input
        user_input = "2 cats and 3 dogs\n"
        expected_output = ['2', '3']

        # Redirect standard input to simulate user input
        with patch('builtins.input', return_value=user_input):
            # Call the function and check the output
            self.assertEqual(get_digit_words(), expected_output)

if __name__ == '__main__':
    unittest.main()
