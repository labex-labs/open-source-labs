# 练习4.10：使用getattr()的示例

`getattr()` 是读取属性的另一种机制。它可用于编写极其灵活的代码。首先，试试这个示例：

```python
>>> import stock
>>> s = stock.Stock('GOOG', 100, 490.1)
>>> columns = ['name','shares']
>>> for colname in columns:
        print(colname, '=', getattr(s, colname))

name = GOOG
shares = 100
>>>
```

仔细观察，输出数据完全由 `columns` 变量中列出的属性名决定。

在 `tableformat.py` 文件中，采用这个思路并将其扩展为一个通用函数 `print_table()`，该函数用于打印一个表格，展示任意对象列表中用户指定的属性。与之前的 `print_report()` 函数一样，`print_table()` 也应该接受一个 `TableFormatter` 实例来控制输出格式。它的工作方式如下：

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('txt')
>>> print_table(portfolio, ['name','shares'], formatter)
      name     shares
---------- ----------
        AA        100
       IBM         50
       CAT        150
      MSFT        200
        GE         95
      MSFT         50
       IBM        100

>>> print_table(portfolio, ['name','shares', 'price'], formatter)
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
>>>
```
