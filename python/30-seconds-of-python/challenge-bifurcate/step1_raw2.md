# Bifurcate List

## Introduction

In Python, we can split a list into two groups based on a given filter. This can be done using a list comprehension and the `zip()` function. In this challenge, you will be asked to write a function that takes a list and a filter as input and returns two lists, one containing the elements that pass the filter and the other containing the elements that do not.

## Problem

Write a function `bifurcate(lst, filter)` that takes a list `lst` and a filter `filter` as input and returns a list of two lists. The first list should contain the elements of `lst` that pass the filter, and the second list should contain the elements that do not.

To implement this function, you can use a list comprehension and the `zip()` function. The `zip()` function takes two or more lists as input and returns a list of tuples, where each tuple contains the corresponding elements from each list. For example, `zip([1, 2, 3], [4, 5, 6])` returns `[(1, 4), (2, 5), (3, 6)]`.

You can use this function to iterate over both `lst` and `filter` simultaneously and add the elements to the appropriate list based on whether they pass the filter or not.

## Example

```python
bifurcate(['beep', 'boop', 'foo', 'bar'], [True, True, False, True])
# Output: [['beep', 'boop', 'bar'], ['foo']]
```

In the above example, the filter is `[True, True, False, True]`. The first two elements of `lst` pass the filter, so they are added to the first list. The third element does not pass the filter, so it is added to the second list. The fourth element passes the filter, so it is added to the first list.

## Summary

In this challenge, you learned how to split a list into two groups based on a given filter. You used a list comprehension and the `zip()` function to iterate over both the list and the filter simultaneously and add the elements to the appropriate list based on whether they pass the filter or not.
