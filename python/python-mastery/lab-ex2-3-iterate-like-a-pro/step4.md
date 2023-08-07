# Using the zip() function

The `zip()` function is most commonly used to pair data. For example,
recall that you created a `headers` variable:

```python
>>> headers
['name', 'shares', 'price']
>>>
```

This might be useful to combine with the other row data:

```python
>>> row = rows[0]
>>> row
['AA', '100', '32.20']
>>> for col, val in zip(headers, row):
        print(col, val)

name AA
shares 100
price 32.20
>>>
```

Or maybe you can use it to make a dictionary:

```python
>>> dict(zip(headers, row))
{'name': 'AA', 'shares': '100', 'price': '32.20'}
>>>
```

Or maybe a sequence of dictionaries:

```python
>>> for row in rows:
        record = dict(zip(headers, row))
        print(record)

{'name': 'AA', 'shares': '100', 'price': '32.20'}
{'name': 'IBM', 'shares': '50', 'price': '91.10'}
{'name': 'CAT', 'shares': '150', 'price': '83.44'}
{'name': 'MSFT', 'shares': '200', 'price': '51.23'}
{'name': 'GE', 'shares': '95', 'price': '40.37'}
{'name': 'MSFT', 'shares': '50', 'price': '65.10'}
{'name': 'IBM', 'shares': '100', 'price': '70.44'}
>>>
```
