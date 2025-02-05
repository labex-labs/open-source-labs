# 表格输出

在练习3.1中，你编写了一个函数 `print_portfolio()`，它生成了格式良好的表格。该函数是专门为 `Stock` 对象列表定制的。然而，使用(b)部分中的技术，可以将其完全通用化，以处理任何对象列表。

创建一个名为 `tableformat.py` 的新模块。在该程序中，编写一个函数 `print_table()`，它接受一个对象序列（列表）、一个属性名列表，并打印出格式良好的表格。例如：

```python
>>> import stock
>>> import tableformat
>>> portfolio = stock.read_portfolio('portfolio.csv')
>>> tableformat.print_table(portfolio, ['name','shares','price'])
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44

>>> tableformat.print_table(portfolio,['shares','name'])
    shares       name
---------- ----------
       100         AA
        50        IBM
       150        CAT
       200       MSFT
        95         GE
        50       MSFT
       100        IBM
>>>
```

为简单起见，让 `print_table()` 函数在10个字符宽的列中打印每个字段。
