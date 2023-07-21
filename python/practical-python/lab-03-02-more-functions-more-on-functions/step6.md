# Multiple Return Values

Functions can only return one value. However, a function may return
multiple values by returning them in a tuple.

```python
def divide(a,b):
    q = a // b      # Quotient
    r = a % b       # Remainder
    return q, r     # Return a tuple
```

Usage example:

```python
x, y = divide(37,5) # x = 7, y = 2

x = divide(37, 5)   # x = (7, 2)
```
