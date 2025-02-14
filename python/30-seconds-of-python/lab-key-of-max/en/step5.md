# Testing with All Negative Values

As a final test, let's handle a case where all the values in the dictionary are negative. Add this method to `TestKeyOfMax`:

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

This test ensures that our function correctly identifies the _least negative_ value (which is the maximum in this case) and returns its associated key.

Run your tests one last time (`python3 test_key_of_max.py`). All four tests should pass. This gives us high confidence that our function is working correctly.

Your complete `test_key_of_max.py` should now look like this:

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```
