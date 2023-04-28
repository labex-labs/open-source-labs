import unittest
import sys
sys.path.append("/home/labex/project")
from decapitalize import *

def decapitalize(s, upper_rest = False):
  return ''.join([s[:1].lower(), (s[1:].upper() if upper_rest else s[1:])])

class TestDecapitalize(unittest.TestCase):
  
  def test_all_lower(self):
    self.assertEqual(decapitalize("hello"), "hello")
    
  def test_first_upper(self):
    self.assertEqual(decapitalize("Hello"), "hello")
    
  def test_all_upper(self):
    self.assertEqual(decapitalize("HELLO"), "hello")
    
  def test_upper_rest(self):
    self.assertEqual(decapitalize("Hello", True), "hELLO")
    
  def test_empty_string(self):
    self.assertEqual(decapitalize(""), "")