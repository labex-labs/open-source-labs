# Looping over integers

If you need to count, use `range()`.

```python
for i in range(100):
    # i = 0,1,...,99
```

The syntax is `range([start,] end [,step])`

```python
for i in range(100):
    # i = 0,1,...,99
for j in range(10,20):
    # j = 10,11,..., 19
for k in range(10,50,2):
    # k = 10,12,...,48
    # Notice how it counts in steps of 2, not 1.
```

- The ending value is never included. It mirrors the behavior of slices.
- `start` is optional. Default `0`.
- `step` is optional. Default `1`.
- `range()` computes values as needed. It does not actually store a large range of numbers.
