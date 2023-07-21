# Reading Attributes

Suppose you read an attribute on an instance.

```python
x = obj.name
```

The attribute may exist in two places:

- Local instance dictionary.
- Class dictionary.

Both dictionaries must be checked. First, check in local `__dict__`.
If not found, look in `__dict__` of class through `__class__`.

```python
>>> s = Stock(...)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

This lookup scheme is how the members of a _class_ get shared by all instances.
