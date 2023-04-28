# Deep Flatten List

## Problem

Write a function `deep_flatten(lst)` that takes a list `lst` as an argument and returns a new list that is the deep flattened version of `lst`. The function should use recursion and the `isinstance()` function with `collections.abc.Iterable` to check if an element is iterable. If an element is iterable, the function should apply `deep_flatten()` recursively to that element. Otherwise, the function should return a list containing only that element.

## Example

```python
deep_flatten([1, [2], [[3], 4], 5]) # [1, 2, 3, 4, 5]
deep_flatten([1, [2, [3, [4]]]]) # [1, 2, 3, 4]
deep_flatten([1, 2, 3, 4]) # [1, 2, 3, 4]
deep_flatten([]) # []
```
