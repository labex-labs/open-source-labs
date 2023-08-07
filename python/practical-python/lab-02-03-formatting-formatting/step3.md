# Dictionary Formatting

You can use the `format_map()` method to apply string formatting to a dictionary of values:

```python
>>> s = {
    'name': 'IBM',
    'shares': 100,
    'price': 91.1
}
>>> '{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)
'       IBM        100      91.10'
>>>
```

It uses the same codes as `f-strings` but takes the values from the supplied dictionary.
