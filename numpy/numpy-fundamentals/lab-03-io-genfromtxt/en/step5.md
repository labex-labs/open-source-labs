# Setting the Data Type

The `dtype` argument is used to control how the strings are converted to other types. It can be a single type, a sequence of types, a comma-separated string, a dictionary, a sequence of tuples, an existing `numpy.dtype` object, or `None` to determine the type from the data itself.

```python
np.genfromtxt(StringIO(data), dtype=float)
```
