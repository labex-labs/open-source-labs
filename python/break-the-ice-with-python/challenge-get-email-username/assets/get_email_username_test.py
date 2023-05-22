from unittest.mock import patch
import unittest
import sys

sys.path.append("/home/labex/project")

from get_email_username import GetEmailUsername

class TestGetEmailUsername(unittest.TestCase):
    def test_get_email_username(self):
        # Simulate user input
        user_input = "john.doe@example.com\n"
        expected_output = "john.doe"

        # Redirect standard input to simulate user input
        with patch('builtins.input', return_value=user_input):
            # Call the function and check the output
            self.assertEqual(GetEmailUsername(), expected_output)


if __name__ == '__main__':
    unittest.main()
