# Reconciling Type Validation with Class Variables

Currently, our `Stock` class uses both the `_types` class variable and property setters for type handling. To improve consistency and maintainability, we'll reconcile these mechanisms so that they use the same type information.

**Instructions:**

1.  Open the `stock.py` file in the editor.

2.  Modify the property setters to use the types defined in the `_types` class variable:

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, self._types[1]):
            raise TypeError(f"Expected {self._types[1].__name__}")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, self._types[2]):
            raise TypeError(f"Expected {self._types[2].__name__}")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

3.  Save the `stock.py` file.

4.  Create a test script named `test_subclass.py`:

    ```bash
    touch /home/labex/project/test_subclass.py
    ```

5.  Add the following code to the `test_subclass.py` file:

    ```python
    from stock import Stock
    from decimal import Decimal

    # Create a subclass with different types
    class DStock(Stock):
        _types = (str, int, Decimal)

    # Test the base class
    s = Stock('GOOG', 100, 490.10)
    print(f"Stock: {s.name}, Shares: {s.shares}, Price: {s.price}, Cost: {s.cost}")

    # Test valid update with float
    try:
        s.price = 500.25
        print(f"Updated Stock price: {s.price}, Cost: {s.cost}")
    except Exception as e:
        print(f"Error updating Stock price: {e}")

    # Test the subclass with Decimal
    ds = DStock('AAPL', 50, Decimal('142.50'))
    print(f"DStock: {ds.name}, Shares: {ds.shares}, Price: {ds.price}, Cost: {ds.cost}")

    # Test invalid update with float (should require Decimal)
    try:
        ds.price = 150.75
        print(f"Updated DStock price: {ds.price}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")

    # Test valid update with Decimal
    try:
        ds.price = Decimal('155.25')
        print(f"Updated DStock price: {ds.price}, Cost: {ds.cost}")
    except Exception as e:
        print(f"Error updating DStock price: {e}")
    ```

6.  Run the test script:

    ```bash
    python /home/labex/project/test_subclass.py
    ```

    You should see that the base `Stock` class accepts float values for the price, while the `DStock` subclass requires `Decimal` values.
