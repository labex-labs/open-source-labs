# Assigning Values to Indexed Arrays

You can assign values to specific elements or subsets of elements in an array using indexing. The value being assigned must be shape consistent with the indexed array.

```python
x = np.arange(10)
x[2:7] = 1
print(x)  # Output: [0, 1, 1, 1, 1, 1, 7, 8, 9]

x = np.arange(10)
x[2:7] = np.arange(5)
print(x)  # Output: [0, 1, 0, 1, 2, 3, 7, 8, 9]
```
