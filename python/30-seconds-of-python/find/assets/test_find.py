import unittest
from find import *

class TestFind(unittest.TestCase):
    def test_find(self):
        lst = [1, 2, 3, 4, 5]
        fn = lambda x: x > 3
        self.assertEqual(find(lst, fn), 4)
        
        lst = ['apple', 'banana', 'cherry']
        fn = lambda x: 'a' in x
        self.assertEqual(find(lst, fn), 'apple')
        
        lst = [True, False, False]
        fn = lambda x: x == True
        self.assertEqual(find(lst, fn), True)
        
if __name__ == '__main__':
    unittest.main()