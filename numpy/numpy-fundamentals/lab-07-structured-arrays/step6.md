# Creating a Record Array

A record array is a subclass of ndarray that allows access to fields by attribute instead of index. We can create a record array using the `np.rec.array` function.

```python
# Create a record array
recordarr = np.rec.array([('Alice', 25), ('Bob', 30)], dtype=[('name', 'U10'), ('age', int)])
```
