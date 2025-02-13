# Filter Non-Unique List Values

## Problem

Write a Python function called `filter_non_unique(lst)` that takes a list as an argument and returns a new list with only the unique values. To solve this problem, you can follow these steps:

1. Use the `collections.Counter` method to get the count of each value in the list.
2. Use a list comprehension to create a list containing only the unique values.

## Example

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
filter_non_unique(['apple', 'banana', 'apple', 'orange', 'pear', 'banana']) # ['orange', 'pear']
```
