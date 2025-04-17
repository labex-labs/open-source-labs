# Implementing Private Attributes

In Python, when we design a class, there are certain attributes that are only meant to be used within the class itself. These attributes are part of the class's internal implementation. To indicate this to other developers, we follow a naming convention. We prefix these internal attributes with an underscore (`_`). This is like a sign that says these attributes are not part of the public API. The public API is the set of methods and attributes that other parts of the code are supposed to interact with. So, attributes with an underscore should not be accessed directly from outside the class.

Let's take a look at the current `Stock` class in the `stock.py` file. This class is used to represent stocks, and it has a class variable named `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

The `types` class variable is used inside the class to convert row data. For example, when we get data in a row, we use these types to convert the data into the correct format. Since this is just an implementation detail and not something that other parts of the code should directly interact with, we should mark it as private.

## Instructions:

1. First, we need to open the `stock.py` file in the editor. 

2. Now, we are going to modify the `types` class variable. We add a leading underscore to it, making it `_types`. This change indicates that this variable is private and should not be accessed directly from outside the class.

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Rest of the class...
   ```

3. After renaming the variable, we need to update the `from_row` method. This method uses the `types` variable to convert row data. Now that we have renamed it to `_types`, we need to update the method accordingly.

   ```python
   @classmethod
   def from_row(cls, row):
       values = [func(val) for func, val in zip(cls._types, row)]
       return cls(*values)
   ```

4. Once we have made these changes, we need to save the file. Saving the file ensures that our changes are stored and can be used later.

5. To test our changes, we are going to create a Python script called `test_stock.py`. We can create the file in the editor using the following command.

   ```bash
   touch /home/labex/project/test_stock.py
   ```

6. Now, we add the following code to the `test_stock.py` file. This code creates instances of the `Stock` class, both directly and using the `from_row` method. It then prints out information about these instances, such as the name, number of shares, price, and cost.

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

7. Finally, we run the test script using the following command in the terminal. This will execute the code in the `test_stock.py` file and show us the output.

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
