# Dictionary/Class Growth

Python dictionaries (and classes) allow up to 5 values to be stored
before their reserved memory doubles. Investigate by making a dictionary
and adding a few more values to it:

```python
>>> row = { 'route': '22', 'date': '01/01/2001', 'daytype': 'U', 'rides': 7354 }
>>> sys.getsizeof(row)
>>> sys.getsizeof(row)
240
>>> row['a'] = 1
>>> sys.getsizeof(row)
240
>>> row['b'] = 2
>>> sys.getsizeof(row)
368
>>>
```

Does the memory go down if you delete the item you just added?

Food for thought: If you are creating large numbers of records,
representing each record as a dictionary might not be the most
efficient approach--you could be paying a heavy price for the convenience
of having a dictionary. It might be better to consider the use of tuples,
named tuples, or classes that define `__slots__`.
