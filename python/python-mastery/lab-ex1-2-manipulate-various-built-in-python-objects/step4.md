# Part 4 : Dictionaries

In last few parts, you've simply worked with stock symbols. However,
suppose you wanted to map stock symbols to other data such as the
price? Use a dictionary:

```python
>>> prices = { 'IBM': 91.1, 'GOOG': 490.1, 'AAPL':312.23 }
>>>
```

A dictionary maps keys to values. Here's how to access:

```python
>>> prices['IBM']
91.1
>>> prices['IBM'] = 123.45
>>> prices['HPQ'] = 26.15
>>> prices
{'GOOG': 490.1, 'AAPL': 312.23, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```

To get a list of keys, use this:

```python
>>> list(prices)
['GOOG', 'AAPL', 'IBM', 'HPQ']
>>>
```

To delete a value, use `del`

```python
>>> del prices['AAPL']
>>> prices
{'GOOG': 490.1, 'IBM': 123.45, 'HPQ': 26.15}
>>>
```
