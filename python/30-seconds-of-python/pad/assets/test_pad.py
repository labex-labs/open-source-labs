import unittest
import sys
sys.path.append("/home/labex/project")
from pad import *

class TestPad(unittest.TestCase):

    def test_pad(self):
        self.assertEqual(pad("hello", 10), "  hello   ")
        self.assertEqual(pad("world", 15, '-'), "-----world-----")
        self.assertEqual(pad("python", 12, '*'), "***python***")

if __name__ == '__main__':
    unittest.main()