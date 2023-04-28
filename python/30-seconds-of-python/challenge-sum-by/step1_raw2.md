# Sum List Based on Function

## Introduction

In Python, we can use the `map()` function to apply a function to each element of a list and return a new list with the modified values. We can also use the `sum()` function to calculate the sum of a list. In this challenge, you will need to write a function that takes a list and a function as arguments, maps each element of the list to a value using the provided function, and returns the sum of the values.

## Problem

Write a function `sum_by(lst, fn)` that takes a list `lst` and a function `fn` as arguments. The function should map each element of the list to a value using the provided function, and return the sum of the values.

### Example

```py
sum_by([{ 'n': 4 }, { 'n': 2 }, { 'n': 8 }, { 'n': 6 }], lambda v : v['n']) # 20
```

In the example above, the `sum_by()` function takes a list of dictionaries and a lambda function that extracts the value of the `'n'` key from each dictionary. The function maps each dictionary to its `'n'` value and returns the sum of the values, which is `20`.

## Summary

In this challenge, you learned how to use the `map()` and `sum()` functions to calculate the sum of a list after mapping each element to a value using a provided function. This is a useful technique that can be used in many different scenarios, such as data processing and analysis.