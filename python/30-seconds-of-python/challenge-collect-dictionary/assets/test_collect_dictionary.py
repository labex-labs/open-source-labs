import unittest
import sys
sys.path.append("/home/labex/project")
from collect_dictionary import *
from collections import defaultdict

class TestCollectDictionary(unittest.TestCase):
    
    def test_collect_dictionary(self):
        obj = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
        expected_output = {1: ['a', 'c'], 2: ['b'], 3: ['d']}
        self.assertEqual(collect_dictionary(obj), expected_output)
        
    def test_collect_dictionary_empty(self):
        obj = {}
        expected_output = {}
        self.assertEqual(collect_dictionary(obj), expected_output)
        
    def test_collect_dictionary_same_values(self):
        obj = {'a': 1, 'b': 1, 'c': 1}
        expected_output = {1: ['a', 'b', 'c']}
        self.assertEqual(collect_dictionary(obj), expected_output)
        
if __name__ == '__main__':
    unittest.main()