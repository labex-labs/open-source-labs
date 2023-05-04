# Median

Write a Python function called `find_median` that takes a list of numbers as an argument and returns the median of the list. Your function should perform the following steps:

1. Sort the numbers of the list using `list.sort()`.
2. Find the median, which is either the middle element of the list if the list length is odd or the average of the two middle elements if the list length is even.
3. Return the median.

Your function should not use any built-in Python libraries or functions that directly solve the problem.

```py
def median(list):
  list.sort()
  list_length = len(list)
  if list_length % 2 == 0:
    return (list[int(list_length / 2) - 1] + list[int(list_length / 2)]) / 2
  return float(list[int(list_length / 2)])
```

```py
median([1, 2, 3]) # 2.0
median([1, 2, 3, 4]) # 2.5
```
