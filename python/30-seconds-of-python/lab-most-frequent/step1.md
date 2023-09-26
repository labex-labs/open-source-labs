# Most Frequent Element

Write a Python function called `most_frequent(lst)` that takes a list of integers as input and returns the most frequent element in the list. If there are multiple elements that appear the same number of times and have the highest frequency, return the one that appears first in the list.

To solve this problem, you can follow these steps:

1. Use `set()` to get the unique values in `lst`.
2. Use `max()` to find the element that has the most appearances.

Your function should have the following signature:

```python
def most_frequent(lst: List[int]) -> int:
```

```python
def most_frequent(lst):
  return max(set(lst), key = lst.count)
```

```python
most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]) #2
```
