# Find Keys with Value

## Problem

Write a Python function called `find_keys(dictionary, value)` that takes in a dictionary and a value as arguments and returns a list of all the keys in the dictionary that have the given value. If there are no keys with the given value, the function should return an empty list.

To solve this problem, you can use the `dictionary.items()` method, which returns a generator that yields key-value pairs of the dictionary. You can then use a list comprehension to filter out the keys that have the given value.

## Example

```python
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```

In this example, the `find_keys()` function is called with a dictionary `ages` and a value `10`. The function returns a list of keys that have the value `10`, which are `'Peter'` and `'Anna'`.

