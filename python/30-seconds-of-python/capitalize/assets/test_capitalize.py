import unittest
from capitalize import *

def capitalize(s, lower_rest=False):
    return ''.join([s[:1].upper(), (s[1:].lower() if lower_rest else s[1:])])

class TestCapitalize(unittest.TestCase):
    def test_capitalize_first_letter(self):
        self.assertEqual(capitalize('hello'), 'Hello')
    
    def test_capitalize_all_letters(self):
        self.assertEqual(capitalize('hello', True), 'Hello')
    
    def test_capitalize_empty_string(self):
        self.assertEqual(capitalize(''), '')
    
    def test_capitalize_single_letter(self):
        self.assertEqual(capitalize('h'), 'H')
    
    def test_capitalize_numbers(self):
        self.assertEqual(capitalize('123'), '123')
    
    def test_capitalize_special_characters(self):
        self.assertEqual(capitalize('!@#$'), '!@#$')

if __name__ == '__main__':
    unittest.main()