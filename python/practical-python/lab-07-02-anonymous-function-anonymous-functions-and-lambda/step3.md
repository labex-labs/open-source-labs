# Lambda: Anonymous Functions

Use a lambda instead of creating the function. In our previous
sorting example.

```python
portfolio.sort(key=lambda s: s['name'])
```

This creates an _unnamed_ function that evaluates a _single_ expression.
The above code is much shorter than the initial code.

```python
def stock_name(s):
    return s['name']

portfolio.sort(key=stock_name)

# vs lambda
portfolio.sort(key=lambda s: s['name'])
```
