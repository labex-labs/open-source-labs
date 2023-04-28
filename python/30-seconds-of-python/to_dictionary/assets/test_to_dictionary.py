import unittest
import sys
sys.path.append("/home/labex/project")
from to_dictionary import *

def to_dictionary(keys, values):
    return dict(zip(keys, values))

class TestToDictionary(unittest.TestCase):
    
    def test_to_dictionary(self):
        keys = ['a', 'b', 'c']
        values = [1, 2, 3]
        expected_output = {'a': 1, 'b': 2, 'c': 3}
        self.assertEqual(to_dictionary(keys, values), expected_output)
        
        keys = ['x', 'y', 'z']
        values = [4, 5, 6]
        expected_output = {'x': 4, 'y': 5, 'z': 6}
        self.assertEqual(to_dictionary(keys, values), expected_output)
        
        keys = ['p', 'q', 'r']
        values = ['apple', 'banana', 'cherry']
        expected_output = {'p': 'apple', 'q': 'banana', 'r': 'cherry'}
        self.assertEqual(to_dictionary(keys, values), expected_output)

if __name__ == '__main__':
    unittest.main()