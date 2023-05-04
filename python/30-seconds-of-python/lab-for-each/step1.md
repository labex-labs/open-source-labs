# Execute Function for Each List Element

Write a function `for_each(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`.

```py
def for_each(itr, fn):
  for el in itr:
    fn(el)
```

```py
for_each([1, 2, 3], print) # 1 2 3
```
