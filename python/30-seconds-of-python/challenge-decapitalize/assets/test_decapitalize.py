import unittest
import sys

sys.path.append("/home/labex/project")
from decapitalize import *


def decapitalize(s, upper_rest=False):
    return "".join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])


class TestDecapitalize(unittest.TestCase):
    def test_decapitalize(self):
        self.assertEqual(decapitalize("FooBar"), "fooBar")
        self.assertEqual(decapitalize("FooBar", True), "fOOBAR")


if __name__ == "__main__":
    unittest.main()
