import unittest
from invert_dictionary import *

class TestInvertDictionary(unittest.TestCase):
    
    def test_invert_dictionary(self):
        obj = {'a': 1, 'b': 2, 'c': 3}
        expected_output = {1: 'a', 2: 'b', 3: 'c'}
        self.assertEqual(invert_dictionary(obj), expected_output)
        
        obj = {'cat': 'meow', 'dog': 'bark', 'bird': 'chirp'}
        expected_output = {'meow': 'cat', 'bark': 'dog', 'chirp': 'bird'}
        self.assertEqual(invert_dictionary(obj), expected_output)
        
        obj = {1: 'one', 2: 'two', 3: 'three'}
        expected_output = {'one': 1, 'two': 2, 'three': 3}
        self.assertEqual(invert_dictionary(obj), expected_output)