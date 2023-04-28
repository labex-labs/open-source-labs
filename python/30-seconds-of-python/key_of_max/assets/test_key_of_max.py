import unittest
from key_of_max import *

def key_of_max(d):
    return max(d, key=d.get)

class TestKeyOfMax(unittest.TestCase):
    def test_key_of_max(self):
        self.assertEqual(key_of_max({'a': 1, 'b': 2, 'c': 3}), 'c')
        self.assertEqual(key_of_max({'apple': 5, 'banana': 2, 'orange': 8}), 'orange')
        self.assertEqual(key_of_max({'cat': 3, 'dog': 3, 'fish': 3}), 'cat')

if __name__ == '__main__':
    unittest.main()