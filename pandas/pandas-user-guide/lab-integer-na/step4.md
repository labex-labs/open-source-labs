# Handling Missing Values with pandas.NA

The `IntegerArray` class uses `pandas.NA` as its scalar missing value. When you slice a single element that's missing, it will return `pandas.NA`.

```python
# Create an IntegerArray with a missing value
a = pd.array([1, None], dtype="Int64")

# Slice the second element which is a missing value
missing_value = a[1]
# Output: <NA>
```
