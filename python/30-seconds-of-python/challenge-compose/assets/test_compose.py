import unittest
import sys

sys.path.append("/home/labex/project")
from compose import *
from functools import reduce


def compose(*fns):
    return reduce(lambda f, g: lambda *args: f(g(*args)), fns)


class TestCompose(unittest.TestCase):
    def test_compose(self):
        add_one = lambda x: x + 1
        multiply_two = lambda x: x * 2
        add_one_then_multiply_two = compose(multiply_two, add_one)
        self.assertEqual(add_one_then_multiply_two(1), 4)
        self.assertEqual(add_one_then_multiply_two(2), 6)
        self.assertEqual(add_one_then_multiply_two(3), 8)


if __name__ == "__main__":
    unittest.main()
