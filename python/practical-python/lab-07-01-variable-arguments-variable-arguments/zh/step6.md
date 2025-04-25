# 练习 7.2：将元组和字典作为参数传递

假设你从一个文件中读取了一些数据，并得到了一个这样的元组：

```python
>>> data = ('GOOG', 100, 490.1)
>>>
```

现在，假设你想用这些数据创建一个 `Stock` 对象。如果你试图直接传递 `data`，它是不起作用的：

```python
>>> from stock import Stock
>>> s = Stock(data)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Stock.__init__() missing 2 required positional arguments:'shares' and 'price'
>>>
```

使用 `*data` 可以轻松解决这个问题。试试这个：

```python
>>> s = Stock(*data)
>>> s
Stock('GOOG', 100, 490.1)
>>>
```

如果你有一个字典，你可以使用 `**` 来代替。例如：

```python
>>> data = { 'name': 'GOOG','shares': 100, 'price': 490.1 }
>>> s = Stock(**data)
Stock('GOOG', 100, 490.1)
>>>
```
