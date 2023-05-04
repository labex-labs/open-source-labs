# Find All Matching Indexes

Write a function `find_index_of_all(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments and returns a list of indexes of all elements in `lst` for which `fn` returns `True`.

### Input

- A list `lst` of integers.
- A testing function `fn` that takes an integer as input and returns a boolean value.

### Output

- A list of integers representing the indexes of all elements in `lst` for which `fn` returns `True`.

```py
def find_index_of_all(lst, fn):
  return [i for i, x in enumerate(lst) if fn(x)]
```

```py
find_index_of_all([1, 2, 3, 4], lambda n: n % 2 == 1) # [0, 2]
```
