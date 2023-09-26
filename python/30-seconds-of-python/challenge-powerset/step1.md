# Powerset Challenge

## Problem

Write a Python function called `powerset(iterable)` that takes an iterable as an argument and returns the powerset of the iterable. The function should follow these steps:

1. Convert the given value to a list.
2. Use `range()` and `itertools.combinations()` to create a generator that returns all subsets.
3. Use `itertools.chain.from_iterable()` and `list()` to consume the generator and return a list.

## Example

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
