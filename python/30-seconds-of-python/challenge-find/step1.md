# Find Matching Value

## Problem
Write a function called `find(lst, fn)` that takes a list `lst` and a testing function `fn` as arguments. The function should return the value of the first element in `lst` for which `fn` returns `True`. If no element satisfies the testing function, the function should return `None`.

## Example
```py
find([1, 2, 3, 4], lambda n: n % 2 == 1) # 1
find(['apple', 'banana', 'cherry'], lambda s: s.startswith('b')) # 'banana'
find([2, 4, 6, 8], lambda n: n % 2 == 1) # None
```

