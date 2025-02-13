# Merge Dictionaries

## Problem

Write a function `merge_dictionaries(*dicts)` that takes in two or more dictionaries as arguments and returns a new dictionary that contains all the key-value pairs from the input dictionaries.

Your function should create a new dictionary and loop over the input dictionaries, using `dictionary.update()` to add the key-value pairs from each one to the result.

## Example

```python
ages_one = {
  'Peter': 10,
  'Isabel': 11,
}
ages_two = {
  'Anna': 9
}
merge_dictionaries(ages_one, ages_two)
# { 'Peter': 10, 'Isabel': 11, 'Anna': 9 }
```
