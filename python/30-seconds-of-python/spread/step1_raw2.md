# Spread List

## Introduction
In Python, a list can contain other lists as elements. Sometimes, we need to flatten a list, which means to convert a nested list into a single list that contains all the elements of the original list. One way to do this is by using the spread operator. In this challenge, you will be asked to implement a function that flattens a list using the spread operator.

## Problem
Write a function called `spread(arg)` that takes a list as an argument and returns a new list that contains all the elements of the original list, flattened. If an element of the original list is a list itself, its elements should be added to the new list individually. The function should not modify the original list.

To implement the function, you should loop over the elements of the original list and use the spread operator to add the elements to the new list. If an element is a list, you should use the `extend()` method to add its elements to the new list. If an element is not a list, you should use the `append()` method to add it to the new list.

## Example
```py
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## Summary
In this challenge, you have learned how to use the spread operator to flatten a list in Python. You have also implemented a function that takes a list as an argument and returns a new list that contains all the elements of the original list, flattened. This is a useful technique to know when working with nested lists in Python.