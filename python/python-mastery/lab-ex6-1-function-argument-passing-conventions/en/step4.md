# Restricting Attribute Names

Currently, our `Structure` class allows any attribute to be set on its instances. For beginners, this might seem convenient at first, but it can actually lead to a lot of problems. When you're working with a class, you expect certain attributes to be present and used in a specific way. If users misspell attribute names or try to set attributes that weren't part of the original design, it can cause errors that are hard to find.

## The Need for Attribute Restriction

Let's look at a simple scenario to understand why we need to restrict attribute names. Consider the following code:

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

In the second line, there's a typo. Instead of `shares`, we wrote `share`. In Python, instead of raising an error, it will simply create a new attribute called `share`. This can lead to subtle bugs because you might think you're updating the `shares` attribute, but you're actually creating a new one. This can make your code behave unexpectedly and be very difficult to debug.

## Implementing Attribute Restriction

To solve this problem, we can override the `__setattr__` method. This method is called every time you try to set an attribute on an object. By overriding it, we can control which attributes can be set and which ones can't.

Update your `Structure` class in `structure.py` with the following code:

```python
def __setattr__(self, name, value):
    """
    Restrict attribute setting to only those defined in _fields
    or attributes starting with underscore (private attributes).
    """
    if name.startswith('_'):
        # Allow setting private attributes (starting with '_')
        super().__setattr__(name, value)
    elif name in self._fields:
        # Allow setting attributes defined in _fields
        super().__setattr__(name, value)
    else:
        # Raise an error for other attributes
        raise AttributeError(f'No attribute {name}')
```

Here's how this method works:

1. If the attribute name starts with an underscore (`_`), it's considered a private attribute. Private attributes are often used for internal purposes in a class. We allow these attributes to be set because they're part of the class's internal implementation.
2. If the attribute name is in the `_fields` list, it means it's one of the attributes defined in the class design. We allow these attributes to be set because they're part of the expected behavior of the class.
3. If the attribute name doesn't meet either of these conditions, we raise an `AttributeError`. This tells the user that they're trying to set an attribute that doesn't exist in the class.

## Testing Attribute Restriction

Now that we've implemented the attribute restriction, let's test it to make sure it works as expected. Create a file named `test_attributes.py` with the following code:

```python
# test_attributes.py
from structure import Stock

s = Stock('GOOG', 100, 490.1)

# This should work - valid attribute
print("Setting shares to 50")
s.shares = 50
print(f"Shares is now: {s.shares}")

# This should work - private attribute
print("\nSetting _internal_data")
s._internal_data = "Some data"
print(f"_internal_data is: {s._internal_data}")

# This should fail - invalid attribute
print("\nTrying to set an invalid attribute:")
try:
    s.share = 60  # Typo in attribute name
    print("This should not print")
except AttributeError as e:
    print(f"Error correctly caught: {e}")
```

To run the test, open your terminal and enter the following command:

```bash
python3 test_attributes.py
```

You should see the following output:

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

This output shows that our class now prevents accidental attribute errors. It allows us to set valid attributes and private attributes, but it raises an error when we try to set an invalid attribute.

## The Value of Attribute Restriction

Restricting attribute names is very important for writing robust and maintainable code. Here's why:

1. It helps catch typos in attribute names. If you make a mistake when typing an attribute name, the code will raise an error instead of creating a new attribute. This makes it easier to find and fix errors early in the development process.
2. It prevents attempts to set attributes that don't exist in the class design. This ensures that the class is used as intended and that the code behaves predictably.
3. It avoids the accidental creation of new attributes. Creating new attributes can lead to unexpected behavior and make the code harder to understand and maintain.

By restricting attribute names, we make our code more reliable and easier to work with.
