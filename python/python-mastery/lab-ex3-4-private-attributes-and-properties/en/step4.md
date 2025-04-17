# Using `__slots__` for Memory Optimization

The `__slots__` attribute restricts the attributes a class can have. It prevents adding new attributes to instances and reduces memory usage.

In our `Stock` class, we'll use `__slots__` to:

1.  Restrict attribute creation to only the attributes we've defined.
2.  Improve memory efficiency, especially when creating many instances.

**Instructions:**

1.  Open the `stock.py` file in the editor.
2.  Add a `__slots__` class variable, listing all the private attribute names used by the class:

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Save the file.

4.  Create a test script named `test_slots.py`:

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Add the following code to the `test_slots.py` file:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Run the test script:

    ```bash
    python /home/labex/project/test_slots.py
    ```

    You should see output showing that you can access the defined attributes, but attempting to add a new attribute raises an `AttributeError`.
