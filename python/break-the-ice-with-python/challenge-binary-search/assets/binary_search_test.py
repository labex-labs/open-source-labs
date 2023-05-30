from unittest.mock import patch
import unittest
import sys
sys.path.append("/home/labex/project")
from binary_search import binary_search

class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        lst = [1, 3, 5, 7, 9]
        item = 9
        expected_index = 4
        index = binary_search(lst, item)
        self.assertEqual(index, expected_index)

if __name__ == '__main__':
    unittest.main()
