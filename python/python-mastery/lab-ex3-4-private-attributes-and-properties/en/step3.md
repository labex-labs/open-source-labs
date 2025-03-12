# Implementing Property Validation

Properties in Python are a powerful feature. They not only let you access computed values as if they were regular attributes but also give you control over how these attribute values are retrieved, set, and deleted. This control is extremely useful when you need to add validation to your attributes. Validation ensures that the values assigned to attributes meet specific criteria, which helps maintain the integrity of your data.

In our `Stock` class, we have two important attributes: `shares` and `price`. We want to make sure that `shares` is a non - negative integer and `price` is a non - negative float. To achieve this validation, we'll use property decorators along with getters and setters.

## Instructions:

1. First, you need to open the `stock.py` file in the editor. This is where we'll make all the changes to our `Stock` class. Use the following command in the terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. In Python, we can use private attributes to store the actual values of our class variables. Private attributes are denoted by a leading underscore. Add the private attributes `_shares` and `_price` to the `Stock` class and modify the constructor to use them. The constructor is the method that gets called when you create a new instance of the class. Here's how you do it:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self._shares = shares  # Using private attribute
       self._price = price    # Using private attribute
   ```

3. Now, we'll define properties for `shares` and `price` with proper validation. Properties are defined using the `@property` decorator for the getter method and the `@<property_name>.setter` decorator for the setter method. The getter method is used to retrieve the value of the attribute, and the setter method is used to set the value. Here's the code to add property definitions with validation:

   ```python
   @property
   def shares(self):
       return self._shares

   @shares.setter
   def shares(self, value):
       if not isinstance(value, int):
           raise TypeError("Expected integer")
       if value < 0:
           raise ValueError("shares must be >= 0")
       self._shares = value

   @property
   def price(self):
       return self._price

   @price.setter
   def price(self, value):
       if not isinstance(value, float):
           raise TypeError("Expected float")
       if value < 0:
           raise ValueError("price must be >= 0")
       self._price = value
   ```

4. Update the constructor to use the property setters for validation. This way, whenever a new instance of the `Stock` class is created, the values of `shares` and `price` will be validated automatically. Here's the updated constructor:

   ```python
   def __init__(self, name, shares, price):
       self.name = name
       self.shares = shares  # Using property setter
       self.price = price    # Using property setter
   ```

5. After making all these changes, save the `stock.py` file. This ensures that your changes are preserved.

6. To verify that our validation is working correctly, we'll create a test script. Open a new file named `test_validation.py` in the editor using the following command:

   ```bash
   code /home/labex/project/test_validation.py
   ```

7. Add the following code to the `test_validation.py` file. This code creates a valid `Stock` instance and then tries to update the `shares` and `price` attributes with both valid and invalid values. It also prints the results and any error messages that occur.

   ```python
   from stock import Stock

   # Create a valid stock instance
   s = Stock('GOOG', 100, 490.10)
   print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

   # Test valid updates
   try:
       s.shares = 50  # Valid update
       print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting shares=50: {e}")

   try:
       s.price = 123.45  # Valid update
       print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
   except Exception as e:
       print(f"Error setting price=123.45: {e}")

   # Test invalid updates
   try:
       s.shares = "50"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares='50': {e}")

   try:
       s.shares = -10  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting shares=-10: {e}")

   try:
       s.price = "123.45"  # Invalid type (string)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price='123.45': {e}")

   try:
       s.price = -10.0  # Invalid value (negative)
       print("This line should not execute")
   except Exception as e:
       print(f"Error setting price=-10.0: {e}")
   ```

8. Finally, run the test script using the following command in the terminal:
   ```bash
   python /home/labex/project/test_validation.py
   ```

You should see output that shows successful valid updates and appropriate error messages for invalid updates. This confirms that our property validation is working as expected.
