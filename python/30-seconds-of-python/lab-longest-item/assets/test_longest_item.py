import unittest
import sys

sys.path.append("/home/labex/project")
from longest_item import *


def longest_item(*args):
    return max(args, key=len)


class TestLongestItem(unittest.TestCase):
    def test_longest_item(self):
        self.assertEqual(longest_item("apple", "banana", "orange"), "banana")
        self.assertEqual(longest_item("cat", "dog", "elephant"), "elephant")
        self.assertEqual(longest_item("red", "green", "blue"), "green")
        self.assertEqual(
            longest_item("Python", "Java", "C++", "JavaScript"), "JavaScript"
        )


if __name__ == "__main__":
    unittest.main()
