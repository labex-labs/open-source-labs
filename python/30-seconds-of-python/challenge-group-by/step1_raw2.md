# Group List Elements

## Introduction

In Python, we can group the elements of a list based on a given function. This can be useful in many situations, such as when we want to group a list of words by their length or a list of numbers by their parity. In this challenge, you will be asked to write a function that groups the elements of a list based on a given function.

## Problem

Write a function `group_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments and returns a dictionary where the keys are the results of applying `fn` to the elements of `lst` and the values are lists of elements from `lst` that produce the corresponding key when `fn` is applied to them.

For example, if we have a list of numbers `[6.1, 4.2, 6.3]` and we want to group them by their integer part, we can use the `floor` function from the `math` module as the grouping function. The expected output would be `{4: [4.2], 6: [6.1, 6.3]}`.

## Example

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```

## Summary

In this challenge, you have learned how to group the elements of a list based on a given function. You have also written a function that does this by using a dictionary to store the groups and a loop to populate them. This is a useful technique that can be applied in many different contexts.
