from unittest.mock import patch
import unittest
import sys

sys.path.append("/home/labex/project")
from calculate_mathematical_expression import calculate_mathematical_expression


class TestGenerate(unittest.TestCase):
    def test_calculate_mathematical_expression(self):
        # Test case 1: user_input = '2 + 2'
        user_input = "2 + 2"
        expected_output = 4
        # Redirect standard input to simulate user input
        with patch("builtins.input", return_value=user_input):
            # Call the function and check the output
            self.assertEqual(calculate_mathematical_expression(), expected_output)


if __name__ == "__main__":
    unittest.main()
