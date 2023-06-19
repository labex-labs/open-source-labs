# Advanced Indexing

Advanced indexing is triggered when the selection object `obj` is a non-tuple sequence object, an ndarray (of data type integer or bool), or a tuple with at least one sequence object or ndarray (of data type integer or bool). There are two types of advanced indexing: integer and boolean.

#### Integer Array Indexing

Integer array indexing allows selection of arbitrary items in the array based on their N-dimensional index. Each integer array represents a number of indices into that dimension.

```python
x = np.arange(10, 1, -1)
print(x[np.array([3, 3, 1, 8])])  # Output: [7, 7, 9, 2]
print(x[np.array([3, 3, -3, 8])])  # Output: [7, 7, 4, 2]
```

#### Boolean Array Indexing

Boolean array indexing allows selection of array elements based on a boolean condition. The result is a new array that contains only the elements corresponding to the `True` values of the boolean array.

```python
x = np.array([1., -1., -2., 3])
x[x < 0] += 20
print(x)  # Output: [ 1., 19., 18., 3.]
```
