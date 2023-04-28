import unittest
from roll import *

def roll(lst, offset):
    return lst[-offset:] + lst[:-offset]

class TestRoll(unittest.TestCase):
    def test_roll(self):
        self.assertEqual(roll([1,2,3,4,5], 2), [4,5,1,2,3])
        self.assertEqual(roll([1,2,3,4,5], 0), [1,2,3,4,5])
        self.assertEqual(roll([1,2,3,4,5], 5), [1,2,3,4,5])
        self.assertEqual(roll([1,2,3,4,5], -2), [3,4,5,1,2])
        self.assertEqual(roll([], 2), [])