# 准备工作

在 Python 中，类的一个主要用途是编写能够以各种方式进行扩展/适配的代码。为了说明这一点，在练习 3.2 中，你创建了一个生成表格的函数 `print_table()`。你用它来生成 `portfolio` 列表的输出。例如：

```python
>>> import stock
>>> import reader
>>> import tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
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
>>>
```

假设你希望 `print_table()` 函数能够以任意数量的输出格式（如 CSV、XML、HTML、Excel 等）生成表格。试图一次性修改该函数以支持所有这些输出格式会很麻烦。更好的方法是将与输出相关的格式化代码移到一个类中，并使用继承来实现不同的输出格式。
