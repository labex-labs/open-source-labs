# Get Nested Value

## Introduction
In Python, dictionaries and lists can contain nested values, which can be accessed using a list of selectors. In this challenge, you will create a function that retrieves the value of the nested key indicated by the given selector list from a dictionary or list.

## Problem
Write a function `get(d, selectors)` that takes a dictionary or list `d` and a list of selectors `selectors` as arguments and returns the value of the nested key indicated by the given selector list. If the key does not exist, return `None`.

To implement this function, use `functools.reduce()` to iterate over the `selectors` list. Apply `operator.getitem()` for each key in `selectors`, retrieving the value to be used as the iteratee for the next iteration.

## Example
```py
users = {
  'freddy': {
    'name': {
      'first': 'fred',
      'last': 'smith'
    },
    'postIds': [1, 2, 3]
  }
}
get(users, ['freddy', 'name', 'last']) # 'smith'
get(users, ['freddy', 'postIds', 1]) # 2
get(users, ['freddy', 'age']) # None
```

## Summary
In this challenge, you learned how to retrieve the value of a nested key from a dictionary or list using a list of selectors. You used `functools.reduce()` and `operator.getitem()` to implement the `get()` function.