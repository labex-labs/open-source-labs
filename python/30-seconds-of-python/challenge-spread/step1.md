# Spread List

## Problem
Write a function called `spread(arg)` that takes a list as an argument and returns a new list that contains all the elements of the original list, flattened. If an element of the original list is a list itself, its elements should be added to the new list individually. The function should not modify the original list.

To implement the function, you should loop over the elements of the original list and use the spread operator to add the elements to the new list. If an element is a list, you should use the `extend()` method to add its elements to the new list. If an element is not a list, you should use the `append()` method to add it to the new list.

## Example
```py
spread([1, 2, 3, [4, 5, 6], [7], 8, 9]) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

