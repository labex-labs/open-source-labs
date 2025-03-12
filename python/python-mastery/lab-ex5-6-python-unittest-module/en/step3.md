# Testing for Exceptions

Testing is a crucial part of software development, and one important aspect of it is to ensure that your code can handle error conditions properly. In Python, the `unittest` module provides a convenient way to test if specific exceptions are raised as expected.

1. Open the `teststock.py` file. We're going to add some test methods that are designed to check for exceptions. These tests will help us make sure that our code behaves correctly when it encounters invalid input.

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

Now, let's understand how these exception tests work.

- The `with self.assertRaises(ExceptionType):` statement creates a context manager. This context manager checks if the code inside the `with` block raises the specified exception.
- If the expected exception is raised within the `with` block, the test passes. This means that our code is correctly detecting the invalid input and raising the appropriate error.
- If no exception is raised or a different exception is raised, the test fails. This indicates that our code might not be handling the invalid input as expected.

These tests are designed to verify the following scenarios:

- Setting the `shares` attribute to a string should raise a `TypeError` because `shares` should be a number.
- Setting the `shares` attribute to a negative number should raise a `ValueError` since the number of shares cannot be negative.
- Setting the `price` attribute to a string should raise a `TypeError` because `price` should be a number.
- Setting the `price` attribute to a negative number should raise a `ValueError` as the price cannot be negative.
- Attempting to set a non-existent attribute `share` (note the missing 's') should raise an `AttributeError` because the correct attribute name is `shares`.

2. After adding these test methods, save the `teststock.py` file. Then, run all the tests using the following command in your terminal:

```bash
python3 teststock.py
```

If everything is working correctly, you should see output indicating that all 12 tests have passed. The output will look like this:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

The twelve dots represent all the tests you've written so far. There were 7 tests from the previous step, and we've just added 5 new ones. This output shows that your code is handling exceptions as expected, which is a great sign of a well-tested program.
