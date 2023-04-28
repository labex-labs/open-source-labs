import unittest
import sys
sys.path.append("/home/labex/project")
from unique_elements import *

def unique_elements(li):
    return list(set(li))

class TestUniqueElements(unittest.TestCase):
    def test_unique_elements(self):
        self.assertEqual(unique_elements([1, 2, 3, 3, 4]), [1, 2, 3, 4])
        self.assertEqual(unique_elements([5, 5, 5, 5]), [5])
        self.assertEqual(unique_elements([]), [])
        self.assertEqual(unique_elements([1, 2, 3]), [1, 2, 3])
        self.assertEqual(unique_elements([1, 1, 1, 2, 2, 3]), [1, 2, 3])

if __name__ == '__main__':
    unittest.main()