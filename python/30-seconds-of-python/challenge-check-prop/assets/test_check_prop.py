import unittest
import sys

sys.path.append("/home/labex/project")
from check_prop import check_prop

class TestCheckProp(unittest.TestCase):
    def test_check_age_true(self):
        check_age = check_prop(lambda x: x >= 18, 'age')
        user = {'name': 'Mark', 'age': 18}
        self.assertTrue(check_age(user))
    
    def test_check_age_false(self):
        check_age = check_prop(lambda x: x >= 18, 'age')
        user = {'name': 'John', 'age': 17}
        self.assertFalse(check_age(user))
    
    def test_check_name(self):
        check_name = check_prop(lambda x: x.startswith('J'), 'name')
        user = {'name': 'John', 'age': 25}
        self.assertTrue(check_name(user))
    
    def test_check_email(self):
        check_email = check_prop(lambda x: '@' in x, 'email')
        user = {'name': 'Alice', 'email': 'alice@example.com'}
        self.assertTrue(check_email(user))
    
    def test_check_phone_number(self):
        check_phone_number = check_prop(lambda x: len(x) == 10, 'phone_number')
        user = {'name': 'Bob', 'phone_number': '1234567890'}
        self.assertTrue(check_phone_number(user))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)