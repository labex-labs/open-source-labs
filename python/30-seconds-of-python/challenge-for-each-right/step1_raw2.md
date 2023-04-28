# Execute function for each list element in reverse

## Introduction

In Python, we can use a `for` loop to iterate over a list and execute a function for each element. However, what if we want to start from the last element and work our way backwards? In this challenge, you will need to create a function that executes the provided function once for each list element, starting from the list's last element.

## Problem

Write a function `for_each_right(itr, fn)` that takes a list `itr` and a function `fn` as arguments. The function should execute `fn` once for each element in `itr`, starting from the last one.

### Example

```py
for_each_right([1, 2, 3], print) # 3 2 1
```

### Constraints

- The function should work for any list and function.
- The function should not modify the original list.

## Summary

In this challenge, you learned how to create a function that executes a provided function for each element in a list, starting from the last one. This can be useful when you need to process a list in reverse order.
