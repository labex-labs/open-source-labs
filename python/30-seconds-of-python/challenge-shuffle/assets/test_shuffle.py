import unittest
import sys
sys.path.append("/home/labex/project")
from shuffle import *
from copy import deepcopy
from random import randint

class TestShuffle(unittest.TestCase):
    
    def test_shuffle(self):
        lst = [1, 2, 3, 4, 5]
        shuffled_lst = shuffle(lst)
        self.assertNotEqual(lst, shuffled_lst)
        self.assertEqual(set(lst), set(shuffled_lst))
        self.assertEqual(len(lst), len(shuffled_lst))
        
        lst = ['a', 'b', 'c', 'd', 'e']
        shuffled_lst = shuffle(lst)
        self.assertNotEqual(lst, shuffled_lst)
        self.assertEqual(set(lst), set(shuffled_lst))
        self.assertEqual(len(lst), len(shuffled_lst))
        
        lst = [True, False, True, False]
        shuffled_lst = shuffle(lst)
        self.assertNotEqual(lst, shuffled_lst)
        self.assertEqual(set(lst), set(shuffled_lst))
        self.assertEqual(len(lst), len(shuffled_lst))
        
        lst = []
        shuffled_lst = shuffle(lst)
        self.assertEqual(lst, shuffled_lst)
        self.assertEqual(len(lst), len(shuffled_lst))
        
if __name__ == '__main__':
    unittest.main()