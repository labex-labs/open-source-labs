# List Similarity

## Problem

Write a function `similarity(a, b)` that takes two lists `a` and `b` as arguments and returns a new list that contains only the elements that exist in both `a` and `b`.

To solve this problem, we can use list comprehension to iterate over the elements of `a` and check if they exist in `b`. If an element exists in both lists, we add it to a new list.

## Example

```py
similarity([1, 2, 3], [1, 2, 4]) # [1, 2]
```

In this example, the function `similarity` takes two lists `[1, 2, 3]` and `[1, 2, 4]` as arguments. The function returns a new list `[1, 2]` that contains only the elements that exist in both lists.
