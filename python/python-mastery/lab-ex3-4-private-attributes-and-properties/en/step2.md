# Converting Methods to Properties

In Python, properties are a powerful feature that allows you to access computed values in a way that's similar to accessing attributes. Normally, when you want to get a value from a method, you need to use parentheses to call that method. However, properties eliminate the need for these parentheses, making your code look cleaner and more consistent with how you access regular attributes.

Let's take a look at our current `Stock` class. It has a `cost()` method that calculates the total cost of the shares. This method multiplies the number of shares by the price per share to give us the total cost. Here's what the `cost()` method looks like:

```python
def cost(self):
    return self.shares * self.price
```

To get the cost value using this method, we have to call it with parentheses, like this:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

But we can make our code better. By converting the `cost()` method to a property, we can access the cost value just like we access other attributes, without using parentheses. Here's how it would look:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

## Instructions:

1. First, we need to open the `stock.py` file in the editor. This is where the `Stock` class is defined, and we'll be making changes to it. Use the following command in the terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Inside the `stock.py` file, we're going to replace the `cost()` method with a property. We'll use the `@property` decorator to do this. The `@property` decorator tells Python that the following method should be treated as a property. Replace the `cost()` method with the following code:

   ```python
   @property
   def cost(self):
       return self.shares * self.price
   ```

3. After making the changes, save the `stock.py` file. This ensures that our modifications are stored and can be used later.

4. Now, we need to create a simple Python script to test our new property. Open a new file named `test_property.py` in the editor using the following command:

   ```bash
   code /home/labex/project/test_property.py
   ```

5. In the `test_property.py` file, we'll add some code to create a `Stock` instance and access the `cost` property. Here's the code you should add:

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

6. Finally, run the test script to see if our property works as expected. Use the following command in the terminal:
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

Notice how we can now access `cost` as an attribute (without parentheses), making our code more consistent with how we access other attributes like `name`, `shares`, and `price`. This makes our code easier to read and maintain.
