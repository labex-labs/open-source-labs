# Implementing Private Attributes

In Python, attributes that are meant to be internal to a class should be prefixed with an underscore (`_`). This naming convention signals to other developers that these attributes are not part of the public API and should not be accessed directly from outside the class.

Let's examine the current `Stock` class in the `stock.py` file:

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

The `types` class variable is used internally by the class for converting row data. Since it's an implementation detail and not intended to be part of the public interface, we should mark it as private.

## Instructions:

1. Open the `stock.py` file in the editor:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Modify the `types` class variable to have a leading underscore, making it `_types`:

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. Update the `from_row` method to use the renamed `_types` variable:

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. Save the file.

5. Test your changes by creating a Python script called `test_stock.py`:

   ```bash
   code /home/labex/project/test_stock.py
   ```

6. Add the following code to `test_stock.py`:

   ```python
   from stock import Stock

   # Create a stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
   print(f"Cost: {s.cost()}")

   # Create from row
   row = ['AAPL', '50', '142.5']
   apple = Stock.from_row(row)
   print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
   print(f"Cost: {apple.cost()}")
   ```

7. Run the test script:
   ```bash
   python /home/labex/project/test_stock.py
   ```

You should see output similar to:

```
Name: GOOG, Shares: 100, Price: 490.1
Cost: 49010.0
Name: AAPL, Shares: 50, Price: 142.5
Cost: 7125.0
```
