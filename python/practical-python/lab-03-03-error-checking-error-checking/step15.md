# Exercise 3.9: Catching exceptions

The `parse_csv()` function you wrote is used to process the entire contents of a file. However, in the real-world, it's possible that input files might have corrupted, missing, or dirty data. Try this experiment:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "fileparse.py", line 36, in parse_csv
    row = [func(val) for func, val in zip(types, row)]
ValueError: invalid literal for int() with base 10: ''
>>>
```

Modify the `parse_csv()` function to catch all `ValueError` exceptions generated during record creation and print a warning message for rows that can't be converted.

The message should include the row number and information about the reason why it failed. To test your function, try reading the file `missing.csv` above. For example:

```python
>>> portfolio = parse_csv('missing.csv', types=[str, int, float])
Row 4: Couldn't convert ['MSFT', '', '51.23']
Row 4: Reason invalid literal for int() with base 10: ''
Row 7: Couldn't convert ['IBM', '', '70.44']
Row 7: Reason invalid literal for int() with base 10: ''
>>>
>>> portfolio
[{'name': 'AA', 'shares': 100, 'price': 32.2}, {'name': 'IBM', 'shares': 50, 'price': 91.1}, {'name': 'CAT', 'shares': 150, 'price': 83.44}, {'name': 'GE', 'shares': 95, 'price': 40.37}, {'name': 'MSFT', 'shares': 50, 'price': 65.1}]
>>>
```
