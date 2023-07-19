# Indexing with NA values

Pandas allows indexing with `NA` values in a boolean array, which are treated as `False`.

```python
# Creating a pandas Series
s = pd.Series([1, 2, 3])

# Creating a boolean array with NA values
mask = pd.array([True, False, pd.NA], dtype="boolean")

# Indexing the series with the boolean array
s[mask] # NA values are treated as False
```

If you want to keep the `NA` values, you can manually fill them with `fillna(True)`.

```python
# Filling NA values with True and indexing the series
s[mask.fillna(True)]
```
