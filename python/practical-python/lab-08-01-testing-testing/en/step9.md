# Exercise 8.1: Writing Unit Tests

In a separate file `test_stock.py`, write a set a unit tests for the `Stock` class. To get you started, here is a small fragment of code that tests instance creation:

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Run your unit tests. You should get some output that looks like this:

    .
    ----------------------------------------------------------------------
    Ran 1 tests in 0.000s

    OK

Once you're satisfied that it works, write additional unit tests that check for the following:

- Make sure the `s.cost` property returns the correct value (49010.0)
- Make sure the `s.sell()` method works correctly. It should decrement the value of `s.shares` accordingly.
- Make sure that the `s.shares` attribute can't be set to a non-integer value.

For the last part, you're going to need to check that an exception is raised. An easy way to do that is with code like this:

```python
class TestStock(unittest.TestCase):
    ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
