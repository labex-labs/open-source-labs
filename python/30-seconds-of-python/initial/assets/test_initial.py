import unittest
import sys
sys.path.append("/home/labex/project")
from initial import *

class TestInitial(unittest.TestCase):
    
    def test_initial(self):
        self.assertEqual(initial([1,2,3]), [1,2])
        self.assertEqual(initial(['a','b','c','d']), ['a','b','c'])
        self.assertEqual(initial([]), [])
        self.assertEqual(initial([5]), [])
        
if __name__ == '__main__':
    unittest.main()