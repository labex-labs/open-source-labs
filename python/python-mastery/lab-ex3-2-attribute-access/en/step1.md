# Understanding Attribute Access in Python

In Python, objects are a fundamental concept. They can store data in attributes, which are like named containers for values. You can think of attributes as variables that belong to an object. There are several ways to access these attributes. The most straightforward and commonly used method is the dot (`.`) notation. However, Python also offers specific functions that give you more flexibility when working with attributes.

## The Dot Notation

Let's start by creating a `Stock` object and see how we can manipulate its attributes using the dot notation. The dot notation is a simple and intuitive way to access and modify an object's attributes.

First, open a new terminal and start the Python interactive shell. This is where you can write and execute Python code line by line.

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

In the code above, we first import the `Stock` class from the `stock` module. Then we create an instance of the `Stock` class named `s`. To get the value of the `name` attribute, we use `s.name`. To change the value of the `shares` attribute, we simply assign a new value to `s.shares`. And if we want to remove an attribute, we use the `del` keyword followed by the attribute name.

## Attribute Access Functions

Python provides four built - in functions that are very useful for attribute manipulation. These functions give you more control when working with attributes, especially when you need to handle them dynamically.

1. `getattr()` - This function is used to get the value of an attribute.
2. `setattr()` - It allows you to set the value of an attribute.
3. `delattr()` - You can use this function to delete an attribute.
4. `hasattr()` - This function checks if an attribute exists in an object.

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

These functions are particularly useful when you need to work with attributes dynamically. Instead of using hard - coded attribute names, you can use variable names. For example, if you have a variable that stores the name of an attribute, you can pass that variable to these functions to perform operations on the corresponding attribute. This gives you more flexibility in your code, especially when dealing with different objects and attributes in a more dynamic way.
