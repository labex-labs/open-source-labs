# Understanding Attribute Access in Python

In Python, objects store data in attributes which can be accessed in several ways. The most common method is using the dot (`.`) notation, but Python also provides specific functions for attribute manipulation.

## The Dot Notation

Let's first create a `Stock` object and manipulate its attributes using the dot notation:

```python
# Open a new terminal and run Python interactive shell
python3

# Import the Stock class from the stock module
from stock import Stock

# Create a Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(s.name)    # Output: 'GOOG'

# Set an attribute
s.shares = 50
print(s.shares)  # Output: 50

# Delete an attribute
del s.shares
# If we try to access s.shares now, we'll get an AttributeError
```

## Attribute Access Functions

Python provides four built-in functions for attribute manipulation:

1. `getattr()` - gets an attribute's value
2. `setattr()` - sets an attribute's value
3. `delattr()` - deletes an attribute
4. `hasattr()` - checks if an attribute exists

Let's see how to use these functions:

```python
# Create a new Stock object
s = Stock('GOOG', 100, 490.1)

# Get an attribute
print(getattr(s, 'name'))       # Output: 'GOOG'

# Set an attribute
setattr(s, 'shares', 50)
print(s.shares)                 # Output: 50

# Check if an attribute exists
print(hasattr(s, 'name'))       # Output: True
print(hasattr(s, 'symbol'))     # Output: False

# Delete an attribute
delattr(s, 'shares')
print(hasattr(s, 'shares'))     # Output: False
```

These functions are particularly useful when you need to work with attributes dynamically, using variable names rather than hard-coded attribute names.
