import unittest
from find_last_index import *

class TestFindLastIndex(unittest.TestCase):
    
    def test_find_last_index(self):
        lst = [1, 2, 3, 4, 5]
        fn = lambda x: x % 2 == 0
        self.assertEqual(find_last_index(lst, fn), 3)
        
        lst = [1, 3, 5, 7, 9]
        fn = lambda x: x % 2 == 0
        self.assertEqual(find_last_index(lst, fn), -1)
        
        lst = ['apple', 'banana', 'cherry']
        fn = lambda x: x.startswith('c')
        self.assertEqual(find_last_index(lst, fn), 2)
        
        lst = ['hello', 'world', 'python']
        fn = lambda x: len(x) > 6
        self.assertEqual(find_last_index(lst, fn), 2)
        
        lst = []
        fn = lambda x: x > 0
        self.assertEqual(find_last_index(lst, fn), -1)