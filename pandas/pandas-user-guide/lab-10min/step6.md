# Data Operations

We can perform operations on dataframes like sorting, applying functions, etc.

```python
# Sorting by an axis
df.sort_index(axis=1, ascending=False)

# Applying a function to the data
df.apply(np.cumsum)
```
