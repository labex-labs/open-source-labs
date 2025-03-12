# Converting Methods to Properties

In Python, properties allow you to access computed values as if they were attributes, without the need for method call syntax (parentheses). This makes your code more elegant and consistent with attribute access.

Currently, our `Stock` class has a `cost()` method that calculates the total cost of the shares:

```python
def cost(self):
    return self.shares * self.price
```

To access this value, we need to call the method with parentheses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

We can improve this by converting the `cost()` method to a property, allowing us to access it without parentheses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## Instructions:

1. Open the `stock.py` file in the editor:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Replace the `cost()` method with a property using the `@property` decorator:

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. Save the file.

4. Create a simple Python script to test the property:

   ```bash
   code /home/labex/project/test_property.py
   ```

5. Add the following code to `test_property.py`:

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

6. Run the test script:
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

Notice how we can now access `cost` as an attribute (without parentheses), making our code more consistent with how we access other attributes like `name`, `shares`, and `price`.
