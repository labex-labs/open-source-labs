# Restricting Attribute Names

Currently, our `Structure` class allows any attribute to be set on its instances. This could lead to errors if users misspell attribute names or try to set attributes that don't exist in the original design.

## The Need for Attribute Restriction

Consider this scenario:

```python
s = Stock('GOOG', 100, 490.1)
s.shares = 50      # Correct attribute name
s.share = 60       # Typo in attribute name - creates a new attribute instead of updating
```

The second line contains a typo - `share` instead of `shares`. Rather than raising an error, Python would simply create a new attribute called `share`, which could lead to subtle bugs.

## Implementing Attribute Restriction

We can override the `__setattr__` method to restrict which attributes can be set. Update your `Structure` class in `structure.py`:

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

This method:

1. Allows private attributes (starting with `_`) to be set
2. Allows attributes defined in `_fields` to be set
3. Raises an error for any other attribute name

## Testing Attribute Restriction

Let's test our implementation. Create a file named `test_attributes.py`:

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

Run the test:

```bash
python3 test_attributes.py
```

Expected output:

```
Setting shares to 50
Shares is now: 50

Setting _internal_data
_internal_data is: Some data

Trying to set an invalid attribute:
Error correctly caught: No attribute share
```

Great! Our class now prevents accidental attribute errors while still allowing legitimate operations.

## The Value of Attribute Restriction

Restricting attribute names helps catch errors early by preventing:

1. Typos in attribute names
2. Attempts to set attributes that don't exist in the class design
3. Accidental creation of new attributes

This makes our code more robust and easier to maintain.
