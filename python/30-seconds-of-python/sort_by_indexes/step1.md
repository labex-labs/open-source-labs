# Sort List by Indexes

## Problem
Write a function `sort_by_indexes(lst, indexes, reverse=False)` that takes two lists as arguments and returns a new list sorted based on the indexes of the second list. The function should have the following parameters:
- `lst`: A list of elements to be sorted.
- `indexes`: A list of integers representing the desired indexes to sort the `lst` by.
- `reverse`: An optional boolean parameter that, when set to `True`, sorts the list in reverse order.

The function should return a new list sorted based on the indexes of the second list.

## Example
```py
a = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
b = [3, 2, 6, 4, 1, 5]
sort_by_indexes(a, b) # ['apples', 'bread', 'eggs', 'jam', 'milk', 'oranges']
sort_by_indexes(a, b, True)
# ['oranges', 'milk', 'jam', 'eggs', 'bread', 'apples']
```

