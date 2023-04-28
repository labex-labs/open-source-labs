import unittest
import sys
sys.path.append("/home/labex/project")
from spread import *

class TestSpread(unittest.TestCase):

    def test_spread(self):
        self.assertEqual(spread([1,2,3,[4,5]]), [1,2,3,4,5])
        self.assertEqual(spread([1,[],2,[3,4],[5]]), [1,2,3,4,5])

if __name__ == '__main__':
    unittest.main()