# Check for Duplicates in List Function

Write a Python function called `has_duplicates(lst)` that takes a list as an argument and returns `True` if the list has any duplicate elements, otherwise returns `False`.

To solve this problem, you can follow these steps:

1. Convert the list to a set to remove duplicates.
2. Compare the length of the set with the length of the original list.
3. If the lengths are equal, then the list has no duplicates, otherwise it has duplicates.

```py
def all_unique(lst):
  return len(lst) == len(set(lst))
```

```py
x = [1, 2, 3, 4, 5, 6]
y = [1, 2, 2, 3, 4, 5]
all_unique(x) # True
all_unique(y) # False
```
