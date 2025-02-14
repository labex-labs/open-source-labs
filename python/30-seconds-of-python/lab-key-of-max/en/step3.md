# Creating Unit Tests: Basic Tests

Now, let's write some tests to make sure our function works correctly. We'll use Python's `unittest` module. Create a new file named `test_key_of_max.py` and add the following code:

```python
import unittest
from key_of_max import key_of_max  # Import our function

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Explanation:

1.  **`import unittest`**: Imports the testing framework.
2.  **`from key_of_max import key_of_max`**: Imports the function we want to test.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: Defines a _test class_. Test classes group related tests together.
4.  **`def test_basic_case(self):`**: Defines a _test method_. Each test method checks a specific aspect of our function. Test method names _must_ start with `test_`.
5.  **`self.assertEqual(...)`**: This is an _assertion_. It checks if two values are equal. If they are not equal, the test fails. In this case, we're checking if `key_of_max({'a': 4, 'b': 0, 'c': 13})` returns `'c'`, which it should.
6.  **`def test_another_case(self):`**: Added another test case to verify the key of the max value which may not be unique.
7.  **`if __name__ == '__main__': unittest.main()`**: This standard Python idiom runs the tests when you execute the script directly (e.g., `python3 test_key_of_max.py`).

Run the tests from your terminal: `python3 test_key_of_max.py`. You should see output indicating that the two tests passed.
