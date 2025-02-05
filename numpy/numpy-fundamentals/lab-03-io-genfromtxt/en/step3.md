# Splitting the Lines into Columns

The `delimiter` argument is used to define how the lines should be split into columns. By default, `numpy.genfromtxt` assumes `delimiter=None`, meaning that the line is split along white spaces (including tabs).

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
