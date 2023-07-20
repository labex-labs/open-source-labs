# Field Access

If the ndarray object is a structured array, the fields of the array can be accessed by indexing the array with strings, dictionary-like.

```python
x = np.array([(1, 2), (3, 4), (5, 6)], dtype=[('a', np.int32), ('b', np.int32)])
print(x['a'])  # Output: [1, 3, 5]
```
