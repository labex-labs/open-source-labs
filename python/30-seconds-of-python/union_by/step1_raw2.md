# List Union Based on Function

## Introduction

In Python, we can use the `set()` function to get the union of two lists. However, sometimes we need to apply a function to each element of both lists before getting the union. In this challenge, you will create a function that returns the union of two lists based on a provided function.

## Problem

Write a function `union_by(a, b, fn)` that takes in two lists `a` and `b`, and a function `fn`. The function should return a list that contains every element that exists in any of the two lists once, after applying the provided function to each element of both.

To solve this problem, you can follow these steps:

1. Create a `set` by applying `fn` to each element in `a`.
2. Use a list comprehension in combination with `fn` on `b` to only keep values not contained in the previously created set, `_a`.
3. Finally, create a `set` from the previous result and `a` and transform it into a `list`.

The function should have the following input parameters:

* `a`: a list of elements
* `b`: a list of elements
* `fn`: a function that takes an element and returns a value

The function should return a list of elements.

## Example

Here's an example of what `union_by()` should do:

```python
from math import floor

union_by([2.1], [1.2, 2.3], floor) # [2.1, 1.2]
```

In this example, `union_by()` takes in two lists `[2.1]` and `[1.2, 2.3]`, and a function `floor()`. The function applies `floor()` to each element of both lists, creating a set of `{2}`. Then, it uses a list comprehension to keep only the values not contained in the set, which is `[1.2]`. Finally, it creates a set from the previous result and `[2.1]`, which is `{1.2, 2.1}`, and transforms it into a list `[1.2, 2.1]`.

## Summary

In this challenge, you learned how to create a function that returns the union of two lists based on a provided function. You also learned how to apply a function to each element of a list, create a set from a list, and transform a set into a list.