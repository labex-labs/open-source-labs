# Basic Indexing

NumPy arrays can be indexed using the standard Python syntax `x[obj]`, where `x` is the array and `obj` is the selection. There are different kinds of indexing available depending on the type of `obj`.

## Single Element Indexing

Single element indexing works exactly like indexing for other standard Python sequences. It is 0-based and accepts negative indices for indexing from the end of the array.

```python
x = np.arange(10)
print(x[2])  # Output: 2
print(x[-2])  # Output: 8
```

## Multidimensional Indexing

Arrays can have multiple dimensions, and indexing works the same way for each dimension. You can access elements in a multidimensional array by separating each dimension's index with a comma.

```python
x = np.arange(10).reshape(2, 5)
print(x[1, 3])  # Output: 8
print(x[1, -1])  # Output: 9
```

## Subdimensional Array Indexing

If you index a multidimensional array with fewer indices than dimensions, you get a subdimensional array. Each index specified selects the array corresponding to the rest of the dimensions selected.

```python
x = np.arange(10).reshape(2, 5)
print(x[0])  # Output: [0, 1, 2, 3, 4]
```
