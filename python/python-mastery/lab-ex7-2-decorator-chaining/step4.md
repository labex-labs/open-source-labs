# Validation (Redux)

In the last exercise, you wrote a `@validated` decorator that enforced
type annotations. For example:

```python
@validated
def add(x: Integer, y:Integer) -> Integer:
    return x + y
```

Make a new decorator `@enforce()` that enforces types specified
via keyword arguments to the decorator instead. For example:

```python
@enforce(x=Integer, y=Integer, return_=Integer)
def add(x, y):
    return x + y
```

The resulting behavior of the decorated function should be identical.
Note: Make the `return_` keyword specify the return type. `return` is
a Python reserved word so you have to pick a slightly different name.

**Discussion**

Writing robust decorators is often a lot harder than it looks.
Recommended reading:
