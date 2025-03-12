# Reconciling Type Validation with Class Variables

In our Python programming journey, we've created a `Stock` class. This class currently has two different ways to handle data types. Understanding these mechanisms is crucial as it helps us manage and organize our code better.

The first mechanism is the `_types` class variable. This variable is used to convert data from rows. When we get data in a row format, the `_types` variable helps us transform that data into the appropriate types for our `Stock` class.

The second mechanism is the property setters. These setters enforce type checking. Whenever we try to set a value for a property in our `Stock` class, the property setters make sure that the value is of the correct type.

However, having two separate mechanisms can make our class hard to maintain. To solve this problem, we need to reconcile these two mechanisms so that they use the same type information. This way, we ensure consistency in our class, and it becomes more reliable when we create subclasses.

## Instructions:

1. First, we need to open the `stock.py` file in the editor. This file contains the code for our `Stock` class. To open it, run the following command in the terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Now, we'll modify the property setters in the `stock.py` file. We want them to use the types defined in the `_types` class variable. This ensures that the type checking in the property setters is consistent with the type conversion done by the `_types` variable. Here's how we modify the property setters:

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

3. After making these changes, save the `stock.py` file. Saving the file ensures that our modifications are preserved.

4. Next, we'll create a test script to verify that subclassing with different types works as expected. To create this script, run the following command in the terminal:

   ```bash
   code /home/labex/project/test_subclass.py
   ```

5. Now, add the following code to the `test_subclass.py` file. This code creates a subclass of the `Stock` class with different types and tests both the base class and the subclass.

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

6. Finally, run the test script to see the results. Run the following command in the terminal:

   ```bash
   python /home/labex/project/test_subclass.py
   ```

When you run the test script, you should see that the base `Stock` class accepts float values for the price, while the `DStock` subclass requires `Decimal` values. This shows that our type reconciliation worked as expected.

### Discussion

By reconciling the type information in our `Stock` class, we've made the class more consistent. Now, the property setters use the same type information as the `from_row` method. This consistency makes the class easier to maintain and extend, especially when creating subclasses.

Although our current `Stock` class implementation might seem complex for a simple concept, it demonstrates important Python techniques for encapsulation and type safety. In real-world applications, you might want to use more advanced tools like dataclasses or third - party libraries to simplify this kind of implementation. These tools can make your code more concise and easier to manage.
