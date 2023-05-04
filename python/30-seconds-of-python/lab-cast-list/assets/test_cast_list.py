import unittest
import sys

sys.path.append("/home/labex/project")
from cast_list import cast_list


class TestCastList(unittest.TestCase):
    def test_string(self):
        self.assertEqual(cast_list("foo"), ["foo"])

    def test_list(self):
        self.assertEqual(cast_list([1]), [1])

    def test_tuple(self):
        self.assertEqual(cast_list(("foo", "bar")), ["foo", "bar"])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
