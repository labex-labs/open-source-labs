import unittest
import sys
sys.path.append("/home/labex/project")
from dict_to_list import *

class TestDictToList(unittest.TestCase):
    def test_dict_to_list(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        expected_output = [('a', 1), ('b', 2), ('c', 3)]
        self.assertEqual(dict_to_list(d), expected_output)

if __name__ == '__main__':
    unittest.main()