# Value Frequencies

## Problem

Write a Python function called `value_frequencies(lst)` that takes a list as an argument and returns a dictionary with the unique values of the list as keys and their frequencies as the values.

To solve this problem, you can follow these steps:

1. Create an empty dictionary to store the frequencies of each unique element.
2. Loop through the list and use `collections.defaultdict` to store the frequencies of each unique element.
3. Use `dict()` to return a dictionary with the unique elements of the list as keys and their frequencies as the values.

Your function should return the dictionary with the unique values and their frequencies.

## Example

```python
value_frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
