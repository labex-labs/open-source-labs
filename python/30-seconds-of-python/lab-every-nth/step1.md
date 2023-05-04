# Every nth element in list

Write a function `every_nth(lst, nth)` that takes a list `lst` and an integer `nth` as arguments and returns a new list containing every `nth` element of the original list.

```py
def every_nth(lst, nth):
  return lst[nth - 1::nth]
```

```py
every_nth([1, 2, 3, 4, 5, 6], 2) # [ 2, 4, 6 ]
```
