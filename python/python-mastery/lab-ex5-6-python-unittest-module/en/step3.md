# Testing for Exceptions

An important part of testing is checking that your code properly handles error conditions. The `unittest` module provides a way to test that specific exceptions are raised when expected.

1. Open the `teststock.py` file and add the following test methods that check for exceptions:

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

Let's understand how these exception tests work:

- `with self.assertRaises(ExceptionType):` creates a context manager that tests if the code inside the `with` block raises the specified exception
- If the expected exception is raised, the test passes
- If no exception is raised or a different exception is raised, the test fails

These tests verify that:

- Setting `shares` to a string raises a `TypeError`
- Setting `shares` to a negative number raises a `ValueError`
- Setting `price` to a string raises a `TypeError`
- Setting `price` to a negative number raises a `ValueError`
- Attempting to set a non-existent attribute `share` raises an `AttributeError`

2. Save the file and run all the tests:

```bash
python3 teststock.py
```

You should now see output indicating that all 12 tests have passed:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

The twelve dots represent all the tests you've written so far (7 from the previous step plus 5 new ones).
