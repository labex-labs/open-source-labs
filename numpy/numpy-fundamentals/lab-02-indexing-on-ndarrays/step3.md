# Slicing and Striding

Basic slicing in NumPy extends Python's slicing concept to N dimensions. It allows you to select a range of elements along each dimension of an array.

## Basic Slicing

Basic slicing occurs when `obj` is a slice object (constructed by `start:stop:step` notation inside of brackets), an integer, or a tuple of slice objects and integers.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[1:7:2])  # Output: [1, 3, 5]
```

## Negative Indices

Negative indices can be used to index from the end of the array. For example, `-1` refers to the last element, `-2` refers to the second-to-last element, and so on.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[-2:10])  # Output: [8, 9]
print(x[-3:3:-1])  # Output: [7, 6, 5, 4]
```

## Default Values for Slicing

If the start index is not specified, it defaults to 0 for positive step values and `-n-1` for negative step values. If the stop index is not specified, it defaults to `n` for positive step values and `-n-1` for negative step values. If the step is not specified, it defaults to 1.

```python
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(x[5:])  # Output: [5, 6, 7, 8, 9]
```
