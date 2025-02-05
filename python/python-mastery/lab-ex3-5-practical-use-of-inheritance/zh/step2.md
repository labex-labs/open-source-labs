# 定义一个通用格式化器类

将以下类定义添加到 `tableformat.py` 文件中：

```python
class TableFormatter:
    def headings(self, headers):
        raise NotImplementedError()

    def row(self, rowdata):
        raise NotImplementedError()
```

现在，修改 `print_table()` 函数，使其接受一个 `TableFormatter` 实例并调用其上的方法来生成输出：

```python
def print_table(records, fields, formatter):
    formatter.headings(fields)
    for r in records:
        rowdata = [getattr(r, fieldname) for fieldname in fields]
        formatter.row(rowdata)
```

这两个类旨在一起使用。例如：

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.TableFormatter()
>>> tableformat.print_table(portfolio, ['name','shares', 'price'], formatter)
Traceback (most recent call last):
...
NotImplementedError
>>>
```

目前，它并没有做太多有趣的事情。你将在下一节中解决这个问题。
