# Map List to Dictionary

## Problem

Write a Python function called `map_dictionary(itr, fn)` that takes two parameters:

- `itr`: a list of values
- `fn`: a function that takes a value as input and returns a value as output

The function should return a dictionary where the key-value pairs consist of the original value as the key and the result of the function as the value.

To solve this problem, follow these steps:

1. Use `map()` to apply `fn` to each value of the list.
2. Use `zip()` to pair original values to the values produced by `fn`.
3. Use `dict()` to return an appropriate dictionary.

## Example

```python
map_dictionary([1, 2, 3], lambda x: x * x) # { 1: 1, 2: 4, 3: 9 }
```

In this example, the `map_dictionary()` function takes a list `[1, 2, 3]` and a lambda function `lambda x: x * x` as input. The lambda function squares the input value. The function returns a dictionary `{ 1: 1, 2: 4, 3: 9 }` where the keys are the original values of the list and the values are the squared values.
