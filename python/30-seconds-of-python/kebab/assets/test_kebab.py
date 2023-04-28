import unittest
from kebab import *

class TestKebab(unittest.TestCase):
    def test_kebab(self):
        self.assertEqual(kebab("helloWorld"), "hello-world")
        self.assertEqual(kebab("camelCaseString"), "camel-case-string")
        self.assertEqual(kebab("snake_case_string"), "snake-case-string")
        self.assertEqual(kebab("kebab-case-string"), "kebab-case-string")
        self.assertEqual(kebab("1234"), "1234")
        self.assertEqual(kebab("Hello World 123"), "hello-world-123")
        self.assertEqual(kebab("ThisIsAReallyLongStringWithNoSpaces"), "this-is-a-really-long-string-with-no-spaces")

if __name__ == '__main__':
    unittest.main()