# Detecting Duplicate Labels

We can check for duplicate labels using `Index.is_unique` and `Index.duplicated()` methods.

```python
# Checking if the index has unique labels
print(df1.index.is_unique)

# Checking if the columns have unique labels
print(df1.columns.is_unique)

# Detecting duplicate labels in the index
print(df1.index.duplicated())
```
