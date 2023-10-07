# Exercise 7.2: Passing tuple and dicts as arguments

Suppose you read some data from a file and obtained a tuple such as this:

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

Now, suppose you wanted to create a `Stock` object from this data. If you try to pass `data` directly, it doesn't work:

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments: 'shares' and 'price'
>>>
```

This is easily fixed using `*data` instead. Try this:

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

If you have a dictionary, you can use `**` instead. For example:

```python
>>> data = { 'name': 'GOOG', 'shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
