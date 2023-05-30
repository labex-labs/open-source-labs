from unittest.mock import patch
from io import StringIO
import unittest
import sys

sys.path.append("/home/labex/project")
from print_special_numbers import speical_numbers_generator


class TestGenerate(unittest.TestCase):
    def test_generate(self):
        # Test case 1: n = 0
        with patch("builtins.input", return_value="0"):
            n = 0
            expected_output = ""
            with StringIO() as buf, patch("sys.stdout", buf):
                resp = [str(i) for i in speical_numbers_generator(n)]
                self.assertEqual(",".join(resp).strip(), expected_output)

        # Test case 2: n = 70
        with patch("builtins.input", return_value="70"):
            n = 70
            expected_output = "0,35,70\n"
            with StringIO() as buf, patch("sys.stdout", buf):
                resp = [str(i) for i in speical_numbers_generator(n)]
                self.assertEqual(",".join(resp) + "\n", expected_output)

        # Test case 3: n = 130
        with patch("builtins.input", return_value="130"):
            n = 130
            expected_output = "0,35,70,105\n"
            with StringIO() as buf, patch("sys.stdout", buf):
                resp = [str(i) for i in speical_numbers_generator(n)]
                self.assertEqual(",".join(resp) + "\n", expected_output)


if __name__ == "__main__":
    unittest.main()
