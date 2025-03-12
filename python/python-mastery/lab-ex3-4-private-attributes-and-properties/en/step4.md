# Using **slots** for Memory Optimization

The `__slots__` attribute is a special attribute that restricts the attributes a class can have. When you define `__slots__`, Python creates a static structure for the instances, which both prevents adding new attributes and reduces memory usage.

In our `Stock` class, we'll use `__slots__` to:

1. Restrict attribute creation to only the attributes we've defined
2. Improve memory efficiency, especially when creating many instances

## Instructions:

1. Open the `stock.py` file in the editor:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Add a `__slots__` class variable listing all the private attribute names used by the class:

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

3. Save the file.

4. Create a test script to verify that `__slots__` is working:

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. Add the following code to `test_slots.py`:

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

6. Run the test script:
   ```bash
   python /home/labex/project/test_slots.py
   ```

You should see output showing that you can access the defined attributes, but attempting to add a new attribute raises an `AttributeError`.

### Understanding `__slots__`

When using `__slots__`, it's important to note:

1. You must list all attributes that will be stored on the instance
2. Only the attributes listed in `__slots__` can be assigned to instances
3. Instances will no longer have a `__dict__` attribute
4. Subclasses will not inherit the `__slots__` of their parent unless they define their own `__slots__`

The primary benefits of using `__slots__` are:

1. **Memory efficiency**: Instances use less memory
2. **Speed**: Attribute access is slightly faster
3. **Prevention of accidental attribute creation**: Helps catch typos and programming errors
