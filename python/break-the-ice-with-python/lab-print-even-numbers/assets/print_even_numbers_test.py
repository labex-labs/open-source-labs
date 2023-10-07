import sys

sys.path.append("/home/labex/project")
from print_even_numbers import even_generator
import unittest
from io import StringIO
from unittest.mock import patch


class Testeven_generator(unittest.TestCase):
    def test_even_generator(self):
        # Test case 1: n = 0
        with patch("builtins.input", return_value="0"):
            n = 0
            expected_output = "0\n"
            with StringIO() as buf, patch("sys.stdout", buf):
                list(even_generator(n))
                self.assertEqual(
                    ",".join(map(str, list(even_generator(n)))) + "\n", expected_output
                )

        # Test case 2: n = 5
        with patch("builtins.input", return_value="5"):
            n = 5
            expected_output = "0,2,4\n"
            with StringIO() as buf, patch("sys.stdout", buf):
                list(even_generator(n))
                self.assertEqual(
                    ",".join(map(str, list(even_generator(n)))) + "\n", expected_output
                )

        # Test case 3: n = 10
        with patch("builtins.input", return_value="10"):
            n = 10
            expected_output = "0,2,4,6,8,10\n"
            with StringIO() as buf, patch("sys.stdout", buf):
                list(even_generator(n))
                self.assertEqual(
                    ",".join(map(str, list(even_generator(n)))) + "\n", expected_output
                )


if __name__ == "__main__":
    unittest.main()
