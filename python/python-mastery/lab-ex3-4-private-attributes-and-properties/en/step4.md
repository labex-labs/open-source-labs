# Using **slots** for Memory Optimization

In Python, the `__slots__` attribute is a special tool that can help you manage your classes more efficiently. It restricts the attributes a class can have. Normally, Python stores instance attributes in a dictionary called `__dict__`, which allows for dynamic addition of new attributes. However, when you define `__slots__`, Python creates a static structure for the instances. This has two main effects: it prevents adding new attributes to the instances, and it reduces memory usage because it doesn't need to maintain the `__dict__`.

In our `Stock` class, we'll use `__slots__` for two important reasons:

1. To restrict attribute creation to only the attributes we've defined. This means that users of the class can't accidentally or intentionally add new attributes that we haven't planned for.
2. To improve memory efficiency, especially when creating many instances. If you have a large number of objects of the `Stock` class, using `__slots__` can save a significant amount of memory.

## Instructions:

1. First, you need to open the `stock.py` file in the editor. This is where we'll make changes to the `Stock` class. Use the following command in the terminal:

   ```bash
   code /home/labex/project/stock.py
   ```

2. Inside the `stock.py` file, we'll add a `__slots__` class variable. This variable should list all the private attribute names used by the class. Here's how you do it:

   ```python
   class Stock:
       # Class variable for type conversions
       _types = (str, int, float)

       # Define slots to restrict attribute creation
       __slots__ = ('name', '_shares', '_price')

       # Rest of the class...
   ```

   By defining `__slots__` like this, we're telling Python that instances of the `Stock` class can only have the attributes `name`, `_shares`, and `_price`.

3. After making these changes, save the file. This ensures that your modifications are preserved.

4. Now, we need to create a test script to verify that `__slots__` is working as expected. Open a new file named `test_slots.py` using the following command:

   ```bash
   code /home/labex/project/test_slots.py
   ```

5. Add the following code to the `test_slots.py` file. This code will create an instance of the `Stock` class, access its existing attributes, and then try to add a new attribute.

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

   The `try` block attempts to add a new attribute `extra` to the `Stock` instance `s`. If `__slots__` is working correctly, this should raise an `AttributeError` because `extra` is not listed in `__slots__`.

6. Finally, run the test script using the following command:
   ```bash
   python /home/labex/project/test_slots.py
   ```

You should see output showing that you can access the defined attributes, but attempting to add a new attribute raises an `AttributeError`. This confirms that `__slots__` is working as intended.

### Understanding `__slots__`

When using `__slots__`, it's important to keep the following points in mind:

1. You must list all attributes that will be stored on the instance. If you forget to list an attribute, you won't be able to assign it to the instance.
2. Only the attributes listed in `__slots__` can be assigned to instances. This helps enforce a strict structure for your objects.
3. Instances will no longer have a `__dict__` attribute. Since `__slots__` creates a static structure, there's no need for the dynamic dictionary.
4. Subclasses will not inherit the `__slots__` of their parent unless they define their own `__slots__`. This means that subclasses have the flexibility to define their own attribute restrictions.

The primary benefits of using `__slots__` are:

1. **Memory efficiency**: Instances use less memory because there's no `__dict__` to store attributes.
2. **Speed**: Attribute access is slightly faster because Python doesn't need to look up the attribute in a dictionary.
3. **Prevention of accidental attribute creation**: Helps catch typos and programming errors by preventing the addition of unexpected attributes.
