# Implementing Private Attributes

In Python, we use a naming convention to indicate that an attribute is intended for internal use within a class. We prefix these attributes with an underscore (`_`). This signals to other developers that these attributes are not part of the public API and should not be accessed directly from outside the class.

Let's look at the current `Stock` class in the `stock.py` file. It has a class variable named `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

The `types` class variable is used internally to convert row data. To indicate that this is an implementation detail, we'll mark it as private.

**Instructions:**

1.  Open the `stock.py` file in the editor. You can use the following command in the terminal to open the file in the WebIDE:

    ```bash
    code /home/labex/project/stock.py
    ```

2.  Modify the `types` class variable by adding a leading underscore, changing it to `_types`.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Update the `from_row` method to use the renamed variable `_types`.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Save the `stock.py` file.

5.  Create a Python script named `test_stock.py` to test your changes. You can create the file in the editor using the following command:

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Add the following code to the `test_stock.py` file. This code creates instances of the `Stock` class and prints information about them.

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

7.  Run the test script using the following command in the terminal:

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
