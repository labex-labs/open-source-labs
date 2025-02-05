# Default Arguments

Sometimes you want an argument to be optional. If so, assign a default value in the function definition.

```python
def read_prices(filename, debug=False):
    ...
```

If a default value is assigned, the argument is optional in function calls.

```python
d = read_prices('prices.csv')
e = read_prices('prices.dat', True)
```

_Note: Arguments with defaults must appear at the end of the arguments list (all non-optional arguments go first)._
