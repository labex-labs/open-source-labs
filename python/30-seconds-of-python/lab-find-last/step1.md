# Find the Last Matching Value

Write a function `find_last(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the value of the last element in `lst` for which `fn` returns `True`. If no element satisfies the testing function, the function should return `None`.

To solve this problem, you should use a list comprehension and `next()` to iterate through the list in reverse order and return the last element that satisfies the testing function.

```py
def find_last(lst, fn):
  return next(x for x in lst[::-1] if fn(x))
```

```py
find_last([1, 2, 3, 4], lambda n: n % 2 == 1) # 3
```
