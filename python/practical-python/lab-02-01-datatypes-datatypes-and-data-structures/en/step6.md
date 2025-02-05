# Tuple Unpacking

To use the tuple elsewhere, you can unpack its parts into variables.

```python
name, shares, price = s
print('Cost', shares * price)
```

The number of variables on the left must match the tuple structure.

```python
name, shares = s     # ERROR
Traceback (most recent call last):
...
ValueError: too many values to unpack
```
