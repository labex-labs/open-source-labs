# Defining Things

Names must always be defined before they get used later.

```python
def square(x):
    return x*x

a = 42
b = a + 2     # Requires that `a` is defined

z = square(b) # Requires `square` and `b` to be defined
```

**The order is important.** You almost always put the definitions of variables and functions near the top.
