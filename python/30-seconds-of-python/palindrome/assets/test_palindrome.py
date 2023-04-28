import unittest
from palindrome import *

class TestPalindrome(unittest.TestCase):
    
    def test_palindrome(self):
        self.assertTrue(palindrome("racecar"))
        self.assertTrue(palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(palindrome("hello world"))
        self.assertTrue(palindrome("Was it a car or a cat I saw?"))
        self.assertTrue(palindrome("No 'x' in Nixon"))
        self.assertFalse(palindrome("This is not a palindrome"))
        
if __name__ == '__main__':
    unittest.main()