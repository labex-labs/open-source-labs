import unittest
import sys
sys.path.append("/home/labex/project")
from check_prop import *

class TestCheckProp(unittest.TestCase):
    
    def test_check_prop(self):
        obj1 = {'name': 'John', 'age': 25}
        obj2 = {'name': 'Jane', 'age': 30}
        
        fn1 = lambda x: x > 20
        fn2 = lambda x: x.startswith('J')
        
        prop1 = 'age'
        prop2 = 'name'
        
        self.assertTrue(check_prop(fn1, prop1)(obj1))
        self.assertTrue(check_prop(fn2, prop2)(obj1))
        self.assertFalse(check_prop(fn1, prop1)(obj2))
        self.assertTrue(check_prop(fn2, prop2)(obj2))