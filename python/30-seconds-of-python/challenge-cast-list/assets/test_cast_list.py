import unittest
import sys
sys.path.append("/home/labex/project")
from cast_list import *


class TestCastList(unittest.TestCase):
    
    def test_tuple(self):
        self.assertEqual(cast_list((1, 2, 3)), [1, 2, 3])
    
    def test_list(self):
        self.assertEqual(cast_list([4, 5, 6]), [4, 5, 6])
    
    def test_set(self):
        self.assertEqual(cast_list({7, 8, 9}), [7, 8, 9])
    
    def test_dict(self):
        self.assertEqual(cast_list({1: 'one', 2: 'two'}), [{1: 'one', 2: 'two'}])
    
    def test_string(self):
        self.assertEqual(cast_list('hello'), ['hello'])
    
    def test_integer(self):
        self.assertEqual(cast_list(123), [123])