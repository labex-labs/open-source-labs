import unittest
import sys
sys.path.append("/home/labex/project")
from key_in_dict import *

class TestKeyInDict(unittest.TestCase):
    
    def test_key_in_dict(self):
        d = {'a': 1, 'b': 2, 'c': 3}
        self.assertTrue(key_in_dict(d, 'a'))
        self.assertFalse(key_in_dict(d, 'd'))
        self.assertTrue(key_in_dict(d, 'c'))
        self.assertFalse(key_in_dict(d, ''))
        
if __name__ == '__main__':
    unittest.main()