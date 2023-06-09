import unittest
import sys

sys.path.append("/home/labex/project")
from n_pairs_parentheses import *


class TestPairParentheses(unittest.TestCase):
    def test_pair_parentheses(self):
        parentheses = Parentheses()
        self.assertRaises(TypeError, parentheses.find_pair, None)
        self.assertRaises(ValueError, parentheses.find_pair, -1)
        self.assertEqual(parentheses.find_pair(0), [])
        self.assertEqual(parentheses.find_pair(1), ["()"])
        self.assertEqual(parentheses.find_pair(2), ["(())", "()()"])
        self.assertEqual(
            parentheses.find_pair(3), ["((()))", "(()())", "(())()", "()(())", "()()()"]
        )
        print("Success: test_pair_parentheses")


def main():
    test = TestPairParentheses()
    test.test_pair_parentheses()


if __name__ == "__main__":
    main()
