# Index of min element

Write a function `min_element_index(arr)` that takes a list of integers `arr` as an argument and returns the index of the element with the minimum value in the list.

To solve this problem, you can use the `min()` function to obtain the minimum value in the list and then use the `list.index()` method to return its index.

```py
def min_element_index(arr):
  return arr.index(min(arr))
```

```py
min_element_index([3, 5, 2, 6, 10, 7, 9]) # 2
```
