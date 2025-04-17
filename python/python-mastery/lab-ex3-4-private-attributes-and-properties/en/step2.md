# Converting Methods to Properties

Properties in Python allow you to access computed values like attributes. This eliminates the need for parentheses when calling a method, making your code cleaner and more consistent.

Currently, our `Stock` class has a `cost()` method that calculates the total cost of the shares.

```python
def cost(self):
    return self.shares * self.price
```

To get the cost value, we have to call it with parentheses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

We can improve this by converting the `cost()` method to a property, allowing us to access the cost value without parentheses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Instructions:**

1.  Open the `stock.py` file in the editor.

2.  Replace the `cost()` method with a property using the `@property` decorator:

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Save the `stock.py` file.

4.  Create a new file named `test_property.py` in the editor:

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Add the following code to the `test_property.py` file to create a `Stock` instance and access the `cost` property:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  Run the test script:

    ```bash
    python /home/labex/project/test_property.py
    ```

    You should see output similar to:

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
