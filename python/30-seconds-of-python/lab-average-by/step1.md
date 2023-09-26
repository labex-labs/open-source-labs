# Mapped List Average

Write a function called `average_by(lst, fn = lambda x: x)` that takes a list `lst` and a function `fn` as arguments. The function `fn` should be used to map each element of the list to a value. The function should then calculate the average of the mapped values and return it.

If the `fn` argument is not provided, the function should use the default identity function, which simply returns the element itself.

Your function should meet the following requirements:

- Use `map()` to map each element to the value returned by `fn`.
- Use `sum()` to sum all of the mapped values, divide by `len(lst)`.
- Omit the last argument, `fn`, to use the default identity function.

Function signature: `def average_by(lst, fn = lambda x: x) -> float:`

```python
def average_by(lst, fn = lambda x: x):
  return sum(map(fn, lst), 0.0) / len(lst)
```

```python
average_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda x: x['n'])
# 5.0
```
