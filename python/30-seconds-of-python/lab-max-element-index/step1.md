# Index of Max Element

Write a function `max_element_index(arr)` that takes a list `arr` as an argument and returns the index of the element with the maximum value. If there are multiple elements with the maximum value, return the index of the first occurrence.

To solve this problem, you can follow these steps:

1. Use the built-in `max()` function to find the maximum value in the list.
2. Use the built-in `list.index()` function to find the index of the first occurrence of the maximum value in the list.
3. Return the index.

```py
def max_element_index(arr):
  return arr.index(max(arr))
```

```py
max_element_index([5, 8, 9, 7, 10, 3, 0]) # 4
```
