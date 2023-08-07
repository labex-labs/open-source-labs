# Logging

Modify the code so that warning messages are issued using the `logging` module. In addition, give optional debugging information indicating the reason for failure. For example:

```python
>>> import reader
>>> import logging
>>> logging.basicConfig(level=logging.DEBUG)
>>> port = reader.read_csv_as_dicts('missing.csv', types=[str, int, float])
WARNING:reader:Row 4: Bad row: ['C', '', '53.08']
DEBUG:reader:Row 4: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 7: Bad row: ['DIS', '50', 'N/A']
DEBUG:reader:Row 7: Reason: could not convert string to float: 'N/A'
WARNING:reader:Row 8: Bad row: ['GE', '', '37.23']
DEBUG:reader:Row 8: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 13: Bad row: ['INTC', '', '21.84']
DEBUG:reader:Row 13: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 17: Bad row: ['MCD', '', '51.11']
DEBUG:reader:Row 17: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 19: Bad row: ['MO', '', '70.09']
DEBUG:reader:Row 19: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 22: Bad row: ['PFE', '', '26.40']
DEBUG:reader:Row 22: Reason: invalid literal for int() with base 10: ''
WARNING:reader:Row 26: Bad row: ['VZ', '', '42.92']
DEBUG:reader:Row 26: Reason: invalid literal for int() with base 10: ''
>>>
```
