# Dictionary Values

## Problem

You are given a flat dictionary, and you need to create a function that returns a flat list of all the values in the dictionary. Your task is to implement the `values_only(flat_dict)` function, which takes a flat dictionary as an argument and returns a list of all the values in the dictionary.

To solve this problem, you can use the `dict.values()` method to return the values in the given dictionary. Then, you can convert the result to a list using the `list()` function.

## Example

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 9,
}
values_only(ages) # [10, 11, 9]
```

