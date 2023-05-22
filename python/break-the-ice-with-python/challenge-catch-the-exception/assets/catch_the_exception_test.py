import unittest
import sys

sys.path.append("/home/labex/project")

from catch_the_exception import divide


class TestDivideFunction(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide()


if __name__ == "__main__":
    unittest.main()
