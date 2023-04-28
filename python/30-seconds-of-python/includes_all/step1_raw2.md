# Check if a List Includes All Values

## Introduction
In Python, you can check if all the elements in one list are included in another list. This can be useful in many situations, such as verifying if a user's input matches a list of valid options. In this challenge, you will create a function that checks if all the values in a given list are included in another list.

## Problem
Write a function called `includes_all(lst, values)` that takes in two lists as parameters. The function should check if all the values in the `values` list are included in the `lst` list. If all the values are included, the function should return `True`. If any of the values are not included, the function should return `False`.

To solve this problem, you should:

1. Use a `for` loop to iterate through each value in the `values` list.
2. Check if the current value is included in the `lst` list using the `in` operator.
3. If the value is not included, return `False`.
4. If all the values are included, return `True`.

## Example
```py
includes_all([1, 2, 3, 4], [1, 4]) # True
includes_all([1, 2, 3, 4], [1, 5]) # False
```

## Summary
In this challenge, you learned how to check if all the values in one list are included in another list. You used a `for` loop to iterate through each value in the `values` list and checked if it was included in the `lst` list using the `in` operator. If all the values were included, the function returned `True`. If any of the values were not included, the function returned `False`.