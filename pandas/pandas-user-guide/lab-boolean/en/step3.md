# Kleene logical operations

Pandas implements Kleene Logic (three-value logic) for logical operations like `&` (and), `|` (or) and `^` (exclusive-or). This differs from how `np.nan` behaves in logical operations.

```python
# Demonstrating the difference in 'or' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") | True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") | True # NA follows Kleene logic

# Demonstrating the difference in 'and' operations between np.nan and NA
pd.Series([True, False, np.nan], dtype="object") & True # np.nan behaves differently
pd.Series([True, False, pd.NA], dtype="boolean") & True # NA follows Kleene logic
```
