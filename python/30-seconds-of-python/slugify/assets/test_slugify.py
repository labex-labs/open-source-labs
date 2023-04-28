import unittest
from slugify import *

class TestSlugify(unittest.TestCase):
  
  def test_lower_case(self):
    self.assertEqual(slugify("Hello World"), "hello-world")
  
  def test_strip(self):
    self.assertEqual(slugify("  Hello World  "), "hello-world")
  
  def test_remove_special_chars(self):
    self.assertEqual(slugify("Hello!@#$%^&*()_+World"), "hello-world")
  
  def test_replace_spaces_and_dashes(self):
    self.assertEqual(slugify("Hello World-This is a Test"), "hello-world-this-is-a-test")
  
  def test_remove_extra_dashes(self):
    self.assertEqual(slugify("---Hello-World---"), "hello-world")

if __name__ == '__main__':
  unittest.main()