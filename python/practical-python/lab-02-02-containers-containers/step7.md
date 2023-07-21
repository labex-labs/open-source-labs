# Composite keys

Almost any type of value can be used as a dictionary key in Python. A dictionary key must be of a type that is immutable.
For example, tuples:

```python
holidays = {
  (1, 1) : 'New Years',
  (3, 14) : 'Pi day',
  (9, 13) : "Programmer's day",
}
```

Then to access:

```python
>>> holidays[3, 14]
'Pi day'
>>>
```

_Neither a list, a set, nor another dictionary can serve as a dictionary key, because lists and dictionaries are mutable._
