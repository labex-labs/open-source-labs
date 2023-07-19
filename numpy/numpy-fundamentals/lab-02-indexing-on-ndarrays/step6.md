# Flat Iterator Indexing

The `x.flat` attribute returns an iterator that can be used to iterate over the entire array in C-contiguous style. This iterator can also be indexed using basic slicing or advanced indexing.

```python
x = np.arange(10)
iterator = x.flat
print(iterator[1:5])  # Output: [1, 2, 3, 4]
```
