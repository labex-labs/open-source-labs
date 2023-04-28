import unittest
import sys
sys.path.append("/home/labex/project")
from when import *

class TestWhen(unittest.TestCase):
    
    def test_when(self):
        def predicate(x):
            return x > 5
        
        def when_true(x):
            return x * 2
        
        result = when(predicate, when_true)(6)
        self.assertEqual(result, 12)
        
        result = when(predicate, when_true)(4)
        self.assertEqual(result, 4)