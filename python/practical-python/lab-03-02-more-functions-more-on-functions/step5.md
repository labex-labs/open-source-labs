# Returning Values

The `return` statement returns a value

```python
def square(x):
    return x * x
```

If no return value is given or `return` is missing, `None` is returned.

```python
def bar(x):
    statements
    return

a = bar(4)      # a = None

# OR
def foo(x):
    statements  # No `return`

b = foo(4)      # b = None
```
