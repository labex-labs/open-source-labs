# Extending Your Test Cases

Now that you've created a basic test case, it's time to expand your testing scope. Adding more tests will help you cover the remaining functionality of the `Stock` class. This way, you can ensure that all aspects of the class work as expected. We'll modify the `TestStock` class to include tests for several methods and properties.

1. Open the `teststock.py` file. Inside the `TestStock` class, we're going to add some new test methods. These methods will test different parts of the `Stock` class. Here's the code you need to add:

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

Let's take a closer look at what each of these tests does:

- `test_create_keyword_args`: This test checks if you can create a `Stock` object using keyword arguments. It verifies that the object's attributes are set correctly.
- `test_cost`: This test checks if the `cost` property of a `Stock` object returns the correct value, which is calculated as the number of shares multiplied by the price.
- `test_sell`: This test checks if the `sell()` method of a `Stock` object correctly updates the number of shares after selling some.
- `test_from_row`: This test checks if the `from_row()` class method can create a new `Stock` instance from a data row.
- `test_repr`: This test checks if the `__repr__()` method of a `Stock` object returns the expected string representation.
- `test_eq`: This test checks if the `__eq__()` method correctly compares two `Stock` objects to see if they are equal.

2. After adding these test methods, save the `teststock.py` file. Then, run the tests again using the following command in your terminal:

```bash
python3 teststock.py
```

If all the tests pass, you should see output like this:

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

The seven dots in the output represent each test. Each dot indicates that a test has passed successfully. So, if you see seven dots, it means all seven tests have passed.
