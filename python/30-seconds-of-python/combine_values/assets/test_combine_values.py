import unittest
from combine_values import *

class TestCombineValues(unittest.TestCase):
    
    def test_combine_values(self):
        dict1 = {'a': 1, 'b': 2}
        dict2 = {'a': 3, 'c': 4}
        dict3 = {'b': 5, 'd': 6}
        expected_output = {'a': [1, 3], 'b': [2, 5], 'c': [4], 'd': [6]}
        self.assertEqual(combine_values(dict1, dict2, dict3), expected_output)

if __name__ == '__main__':
    unittest.main()