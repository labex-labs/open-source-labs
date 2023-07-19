# Comparing Structured Arrays

If the dtypes of two structured arrays are equal, we can compare them using the equality operator (`==`). This will return a boolean array indicating which elements have the same values for all fields.

```python
# Compare two structured arrays
y = np.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
comparison = x == y
```
