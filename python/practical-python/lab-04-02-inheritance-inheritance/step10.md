# `object` base class

If a class has no parent, you sometimes see `object` used as the base.

```python
class Shape(object):
    ...
```

`object` is the parent of all objects in Python.

\*Note: it's not technically required, but you often see it specified as a hold-over from it's required use in Python 2. If omitted, the class still implicitly inherits from `object`.
