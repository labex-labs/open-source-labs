# Операции с данными

Мы можем выполнять операции с DataFrame, такими как сортировка, применение функций и т.д.

```python
# Sorting by an axis
df.sort_index(axis=1, ascending=False)

# Applying a function to the data
df.apply(np.cumsum)
```
