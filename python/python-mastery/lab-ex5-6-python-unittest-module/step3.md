# Unit tests with expected errors

Suppose you wanted to write a unit test that checks for an exception. Here is how you can do it:

```python
class TestStock(unittest.TestCase):
    ...
    def test_bad_shares(self):
        s = stock.Stock('GOOG', 100, 490.1)
        with self.assertRaises(TypeError):
             s.shares = '50'
    ...
```

Using this test as a guide, write unit tests for the following failure modes:

- Test that setting `shares` to a string raises a `TypeError`
- Test that setting `shares` to a negative number raises a `ValueError`
- Test that setting `price` to a string raises a `TypeError`
- Test that setting `price` to a negative number raises a `ValueError`
- Test that setting a non-existent attribute `share` raises an `AttributeError`

In total, you should have around a dozen unit tests when you're done.

**Important Note**

For later use in the course, you will want to have a fully working `stock.py` and `teststock.py` file. Save your work in progress if you have to, but you are strongly encouraged to copy the code from `Solutions/5_6` if things are still broken at this point.

We're going to use the `teststock.py` file as a tool for improving the `Stock` code later. You'll want it on hand to make sure that the new code behaves the same way as the old code.
