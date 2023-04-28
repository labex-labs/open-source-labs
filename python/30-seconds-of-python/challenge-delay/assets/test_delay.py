import unittest
import sys
sys.path.append("/home/labex/project")
from delay import *

class TestDelay(unittest.TestCase):
  
  def test_delay(self):
    def add(a, b):
      return a + b
      
    self.assertEqual(delay(add, 1000, 2, 3), 5)
    
    def multiply(a, b, c):
      return a * b * c
      
    self.assertEqual(delay(multiply, 500, 2, 3, 4), 24)
    
    def greet(name):
      return "Hello, " + name
      
    self.assertEqual(delay(greet, 2000, "John"), "Hello, John")
    
if __name__ == '__main__':
  unittest.main()