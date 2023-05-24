from unittest.mock import patch
import unittest
import sys

sys.path.append("/home/labex/project")

from summation_of_series import summation_of_series


class TestMyCode(unittest.TestCase):
    def test_my_function(self):
        # Simulate user input
        user_input = 5
        expected_output = 3.55

        # Redirect standard input to simulate user input
        with patch("builtins.input", return_value=user_input):
            # Call the function and check the output
            self.assertEqual(summation_of_series(), expected_output)


if __name__ == "__main__":
    unittest.main()
