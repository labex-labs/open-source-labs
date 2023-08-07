# Catching Exceptions

Instead of crashing on bad data, modify the code to issue a warning message
instead. The final result should be a list of the rows that were successfully
converted. For example:

```python
>>> port = read_csv_as_dicts('missing.csv', types=[str, int, float])
Row 4: Bad row: ['C', '', '53.08']
Row 7: Bad row: ['DIS', '50', 'N/A']
Row 8: Bad row: ['GE', '', '37.23']
Row 13: Bad row: ['INTC', '', '21.84']
Row 17: Bad row: ['MCD', '', '51.11']
Row 19: Bad row: ['MO', '', '70.09']
Row 22: Bad row: ['PFE', '', '26.40']
Row 26: Bad row: ['VZ', '', '42.92']
>>> len(port)
20
>>>
```

Note: Making this change may be a bit tricky because of your previous use of the `map()`
built-in function. You may have to abandon that approach since there's no easy way to catch
and handle exceptions in `map()`.
