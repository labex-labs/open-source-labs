# Common operations

To get values from a dictionary use the key names.

```python
>>> print(s['name'], s['shares'])
GOOG 100
>>> s['price']
490.10
>>>
```

To add or modify values assign using the key names.

```python
>>> s['shares'] = 75
>>> s['date'] = '6/6/2007'
>>>
```

To delete a value use the `del` statement.

```python
>>> del s['date']
>>>
```
