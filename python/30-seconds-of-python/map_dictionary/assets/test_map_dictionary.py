import unittest
from map_dictionary import *

def map_dictionary(itr, fn):
    return dict(zip(itr, map(fn, itr)))

class TestMapDictionary(unittest.TestCase):
    
    def test_map_dictionary(self):
        self.assertEqual(map_dictionary([1, 2, 3], lambda x: x*2), {1: 2, 2: 4, 3: 6})
        self.assertEqual(map_dictionary(['a', 'b', 'c'], lambda x: x.upper()), {'a': 'A', 'b': 'B', 'c': 'C'})
        self.assertEqual(map_dictionary([], lambda x: x**2), {})
        
if __name__ == '__main__':
    unittest.main()