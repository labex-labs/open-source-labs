# Improving Object Representation

Our `Structure` class is useful for creating and accessing objects. However, it currently doesn't have a good way to represent itself as a string. When you print an object or view it in the Python interpreter, you want to see a clear and informative display. This helps you understand what the object is and what its values are.

## Understanding Python's Object Representation

In Python, there are two special methods that are used to represent objects in different ways. These methods are important because they allow you to control how your objects are displayed.

- `__str__` - This method is used by the `str()` function and the `print()` function. It provides a human-readable representation of the object. For example, if you have a `Stock` object, the `__str__` method might return something like "Stock: GOOG, 100 shares at $490.1".
- `__repr__` - This method is used by the Python interpreter and the `repr()` function. It gives a more technical and unambiguous representation of the object. The goal of `__repr__` is to provide a string that can be used to recreate the object. For instance, for a `Stock` object, it might return "Stock('GOOG', 100, 490.1)".

Let's add a `__repr__` method to our `Structure` class. This will make it easier to debug our code because we can clearly see the state of our objects.

## Implementing a Good Representation

Now, you need to update your `structure.py` file. You'll add the `__repr__` method to the `Structure` class. This method will create a string that represents the object in a way that can be used to recreate it.

```python
def __repr__(self):
    """
    Return a representation of the object that can be used to recreate it.
    Example: Stock('GOOG', 100, 490.1)
    """
    # Get the class name
    cls_name = type(self).__name__

    # Get all the field values
    values = [getattr(self, name) for name in self._fields]

    # Format the fields and values
    args_str = ', '.join(repr(value) for value in values)

    # Return the formatted string
    return f"{cls_name}({args_str})"
```

Here's what this method does step by step:

1. It gets the class name using `type(self).__name__`. This is important because it tells you what kind of object you're dealing with.
2. It retrieves all the field values from the instance. This gives you the data that the object holds.
3. It creates a string representation with the class name and values. This string can be used to recreate the object.

## Testing the Improved Representation

Let's test our enhanced implementation. Create a new file called `test_repr.py`. This file will create some instances of our classes and print their representations.

```python
# test_repr.py
from structure import Stock, Point, Date

# Create instances
s = Stock('GOOG', 100, 490.1)
p = Point(3, 4)
d = Date(2023, 11, 9)

# Print the representations
print(repr(s))
print(repr(p))
print(repr(d))

# Direct printing also uses __repr__ in the interpreter
print(s)
print(p)
print(d)
```

To run the test, open your terminal and enter the following command:

```bash
python3 test_repr.py
```

You should see the following output:

```
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
Stock('GOOG', 100, 490.1)
Point(3, 4)
Date(2023, 11, 9)
```

This output is much more informative than before. When you see `Stock('GOOG', 100, 490.1)`, you immediately know what the object represents. You could even copy this string and use it to recreate the object in your code.

## The Benefit of Good Representations

A good `__repr__` implementation is very helpful for debugging. When you're looking at objects in the interpreter or logging them during program execution, a clear representation makes it easier to identify issues quickly. You can see the exact state of the object and understand what might be going wrong.
