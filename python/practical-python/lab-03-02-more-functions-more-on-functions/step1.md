# Calling a Function

Consider this function:

```python
def read_prices(filename, debug):
    ...
```

You can call the function with positional arguments:

```
prices = read_prices('prices.csv', True)
```

Or you can call the function with keyword arguments:

```python
prices = read_prices(filename='prices.csv', debug=True)
```
