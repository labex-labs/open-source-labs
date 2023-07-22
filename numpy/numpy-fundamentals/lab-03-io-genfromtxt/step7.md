# Using Missing and Filling Values

The `missing_values` and `filling_values` arguments are used to handle missing data. The `missing_values` argument is used to recognize missing data, and the `filling_values` argument is used to provide a value for missing entries.

```python
np.genfromtxt(StringIO(data), missing_values="N/A", filling_values=0)
```
