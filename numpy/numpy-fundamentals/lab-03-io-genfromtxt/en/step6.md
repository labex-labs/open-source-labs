# Tweaking the Conversion

The `converters` argument allows us to define conversion functions to handle more complex conversions. It accepts a dictionary with column indices or column names as keys and conversion functions as values.

```python
convertfunc = lambda x: float(x.strip(b"%"))/100.
np.genfromtxt(StringIO(data), converters={1: convertfunc})
```
