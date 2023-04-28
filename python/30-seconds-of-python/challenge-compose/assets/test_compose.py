import unittest
import sys

sys.path.append("/home/labex/project")
from compose import compose


class TestCompose(unittest.TestCase):
    def test_compose_two_functions(self):
        add5 = lambda x: x + 5
        multiply = lambda x, y: x * y
        multiply_and_add_5 = compose(add5, multiply)
        self.assertEqual(multiply_and_add_5(5, 2), 15)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
