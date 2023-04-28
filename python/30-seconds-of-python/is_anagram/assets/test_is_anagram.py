import unittest
import sys
sys.path.append("/home/labex/project")
from is_anagram import *
from collections import Counter

def is_anagram(s1, s2):
  return Counter(
    c.lower() for c in s1 if c.isalnum()
  ) == Counter(
    c.lower() for c in s2 if c.isalnum()
  )

class TestAnagram(unittest.TestCase):
    def test_anagram(self):
        self.assertTrue(is_anagram("Listen", "silent"))
        self.assertTrue(is_anagram("Eleven plus two", "Twelve plus one"))
        self.assertFalse(is_anagram("Hello", "World"))
        self.assertFalse(is_anagram("Python", "Java"))

if __name__ == '__main__':
    unittest.main()