# String Formatting

One way to format string in Python 3.6+ is with `f-strings`.

```python
>>> name = 'IBM'
>>> shares = 100
>>> price = 91.1
>>> f'{name:>10s} {shares:>10d} {price:>10.2f}'
'       IBM        100      91.10'
>>>
```

The part `{expression:format}` is replaced.

It is commonly used with `print`.

```python
print(f'{name:>10s} {shares:>10d} {price:>10.2f}')
```
