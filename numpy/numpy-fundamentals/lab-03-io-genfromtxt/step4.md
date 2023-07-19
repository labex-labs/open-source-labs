# Choosing Columns

The `usecols` argument is used to select which columns to import. It accepts a single integer or a sequence of integers corresponding to the indices of the columns to import.

```python
np.genfromtxt(StringIO(data), usecols=(0, -1))
```
