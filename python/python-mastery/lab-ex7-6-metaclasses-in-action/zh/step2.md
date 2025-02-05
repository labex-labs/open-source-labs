# 惊叹不已

试着在这个新文件上运行你的`teststock.py`单元测试。现在它们中的大多数应该都能通过。为了好玩，用一些早期的表格格式化和读取数据的代码来试试你的`Stock`类。一切应该都能正常工作。

```python
>>> from stock import Stock
>>> from reader import read_csv_as_instances
>>> portfolio = read_csv_as_instances('portfolio.csv', Stock)
>>> portfolio
[Stock('AA',100,32.2), Stock('IBM',50,91.1), Stock('CAT',150,83.44), Stock('MSFT',200,51.23), Stock('GE',95,40.37), Stock('MSFT',50,65.1), Stock('IBM',100,70.44)]
>>> from tableformat import create_formatter, print_table
>>> formatter = create_formatter('text')
>>> print_table(portfolio, ['name','shares','price'], formatter)
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

再一次，惊叹于最终的`stock.py`文件，并观察代码看起来多么简洁。只是尽量不要去想`Structure`基类在幕后发生的所有事情。
