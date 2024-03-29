# Sort Dictionary

Write a function called `sort_dict_by_value(d, reverse=False)` that takes a dictionary `d` and sorts it by its values. The function should return a new dictionary with the same keys as the original dictionary, but with the values sorted in ascending order. If the `reverse` parameter is set to `True`, the function should sort the dictionary in descending order.

To solve this problem, you can follow these steps:

1. Use `dict.items()` to get a list of tuple pairs from `d`.
2. Sort the list using a lambda function and `sorted()`.
3. Use `dict()` to convert the sorted list back to a dictionary.
4. Use the `reverse` parameter in `sorted()` to sort the dictionary in reverse order, based on the second argument.

**⚠️ NOTICE:** Dictionary values must be of the same type.

```python
def sort_dict_by_value(d, reverse = False):
  return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))
```

```python
d = {'one': 1, 'three': 3, 'five': 5, 'two': 2, 'four': 4}
sort_dict_by_value(d) # {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
sort_dict_by_value(d, True)
# {'five': 5, 'four': 4, 'three': 3, 'two': 2, 'one': 1}
```
