# Extending Your Test Cases

Now that you have a basic test case, let's add more tests to cover the rest of the `Stock` class functionality. We'll modify the `TestStock` class to include tests for several methods and properties.

1. Open the `teststock.py` file and add the following test methods inside the `TestStock` class:

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

Let's review what each of these tests verifies:

- `test_create_keyword_args`: Tests that you can create a `Stock` using keyword arguments
- `test_cost`: Tests that the `cost` property returns the correct value (shares \* price)
- `test_sell`: Tests that the `sell()` method correctly updates the shares
- `test_from_row`: Tests that the `from_row()` class method creates a new instance from a data row
- `test_repr`: Tests that the `__repr__()` method returns the expected string representation
- `test_eq`: Tests that the `__eq__()` method correctly compares two Stock objects

2. Save the file and run the tests again:

```bash
python3 teststock.py
```

You should see output indicating that all tests have passed:

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

The seven dots (one for each test) show that all tests passed successfully.
