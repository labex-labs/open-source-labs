# Execute function for each list element in reverse

Write a function `for_each_right(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`, starting from the last one.

```py
def for_each_right(itr, fn):
  for el in itr[::-1]:
    fn(el)
```

```py
for_each_right([1, 2, 3], print) # 3 2 1
```
