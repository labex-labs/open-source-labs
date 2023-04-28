# Bifurcate List Based on Function

## Problem

Write a function `bifurcate_by(lst, fn)` that takes a list `lst` and a filtering function `fn` as arguments. The function should split the list into two groups based on the result of the filtering function. If the filtering function returns a truthy value for an element, it should be added to the first group. Otherwise, it should be added to the second group.

Your function should return a list of two lists, where the first list contains all the elements for which the filtering function returned a truthy value, and the second list contains all the elements for which the filtering function returned a falsy value.

Use a list comprehension to add elements to groups, based on the value returned by `fn` for each element.

## Example

```py
bifurcate_by(['beep', 'boop', 'foo', 'bar'], lambda x: x[0] == 'b')
# [ ['beep', 'boop', 'bar'], ['foo'] ]
```

In the example above, the function is called with a list of strings and a filtering function that checks if the first character of each string is 'b'. The function returns a list of two lists, where the first list contains all the strings that start with 'b', and the second list contains all the other strings.
