# Sort Dictionary by Key

## Problem
Write a function `sort_dict_by_key(d, reverse=False)` that takes a dictionary `d` and returns a new dictionary sorted by key. The function should have an optional parameter `reverse` that defaults to `False`. If `reverse` is `True`, the dictionary should be sorted in reverse order.

## Example
```py
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_key(d) # {'five': 5, 'four': 4, 'one': 1, 'three': 3, 'two': 2}
sort_dict_by_key(d, True) # {'two': 2, 'three': 3, 'one': 1, 'four': 4, 'five': 5}
```

