# Filter Unique List Values

Write a Python function called `filter_unique(lst)` that takes a list as an argument and returns a new list with only the non-unique values. To solve this problem, you can follow these steps:

1. Use `collections.Counter` to get the count of each value in the list.
2. Use a list comprehension to create a list containing only the non-unique values.

Your function should satisfy the following requirements:

- The function should take a list as an argument.
- The function should return a new list with only the non-unique values.
- The function should not modify the original list.
- The function should be case-sensitive, meaning that 'a' and 'A' are considered different values.

```python
def filter_unique(lst):
    # your code here
```

```py
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```py
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
