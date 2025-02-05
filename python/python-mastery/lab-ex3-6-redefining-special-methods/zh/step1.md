# 用于表示对象的更好输出

所有 Python 对象都有两种字符串表示形式。第一种表示形式是通过 `str()` 进行字符串转换创建的（`print` 调用此函数）。字符串表示形式通常是对象格式良好的版本，供人类阅读。第二种表示形式是由 `repr()` 创建的对象的代码表示形式（或者简单地在交互式 shell 中查看值时）。代码表示形式通常会显示你为获取该对象而必须键入的代码。以下是一个使用日期的示例：

```python
>>> from datetime import date
>>> d = date(2008, 7, 5)
>>> print(d)              # 使用 str()
2008-07-05
>>> d    # 使用 repr()
datetime.date(2008, 7, 5)
>>>
```

有几种在输出中获取 `repr()` 字符串的技术：

```python
>>> print('The date is', repr(d))
The date is datetime.date(2008, 7, 5)
>>> print(f'The date is {d!r}')
The date is datetime.date(2008, 7, 5)
>>> print('The date is %r' % d)
The date is datetime.date(2008, 7, 5)
>>>
```

修改你创建的 `Stock` 对象，以便 `__repr__()` 方法产生更有用的输出。例如：

```python
>>> goog = Stock('GOOG', 100, 490.10)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

看看当你读取股票投资组合并在进行这些更改后查看结果列表时会发生什么。例如：

```python
>>> import stock, reader
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> portfolio
[Stock('AA', 100, 32.2), Stock('IBM', 50, 91.1), Stock('CAT', 150, 83.44), Stock('MSFT', 200, 51.23),
 Stock('GE', 95, 40.37), Stock('MSFT', 50, 65.1), Stock('IBM', 100, 70.44)]
>>>
```
