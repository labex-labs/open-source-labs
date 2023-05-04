# Find Keys with Value

Write a Python function called `find_keys(dictionary, value)` that takes in a dictionary and a value as arguments and returns a list of all the keys in the dictionary that have the given value. If there are no keys with the given value, the function should return an empty list.

To solve this problem, you can use the `dictionary.items()` method, which returns a generator that yields key-value pairs of the dictionary. You can then use a list comprehension to filter out the keys that have the given value.

```py
def find_keys(dict, val):
  return list(key for key, value in dict.items() if value == val)
```

```py
ages = {
  'Peter': 10,
  'Isabel': 11,
  'Anna': 10,
}
find_keys(ages, 10) # [ 'Peter', 'Anna' ]
```
