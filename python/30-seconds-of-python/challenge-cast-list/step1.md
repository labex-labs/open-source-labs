# Cast to List Challenge

## Problem

Write a function `cast_list(val)` that takes a value as an argument and returns it as a list. If the value is already a list, return it as is. If the value is not a list but is iterable, return it as a list. If the value is not iterable, return it as a single-item list.

## Example

```python
cast_list('foo') # ['foo']
cast_list([1]) # [1]
cast_list(('foo', 'bar')) # ['foo', 'bar']
```
