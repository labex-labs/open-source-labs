# Decorators

Putting wrappers around functions is extremely common in Python.
So common, there is a special syntax for it.

```python
def add(x, y):
    return x + y
add = logged(add)

# Special syntax
@logged
def add(x, y):
    return x + y
```

The special syntax performs the same exact steps as shown above. A decorator is just new syntax.
It is said to _decorate_ the function.
