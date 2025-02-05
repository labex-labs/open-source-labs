# 接口与类型检查

修改`print_table()`函数，使其检查所提供的格式化器实例是否继承自`TableFormatter`。如果不是，则引发`TypeError`。

你的新代码应能捕获如下情况：

```python
>>> import stock, reader, tableformat
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> class MyFormatter:
        def headings(self,headers): pass
        def row(self,rowdata): pass

>>> tableformat.print_table(portfolio, ['name','shares','price'], MyFormatter())
Traceback (most recent call last):
...
TypeError: 期望一个TableFormatter
>>>
```

添加这样的检查可能会给程序增加一定程度的安全性。不过你仍应意识到，在Python中类型检查相当薄弱。即使作为格式化器传递的对象碰巧继承自正确的基类，也不能保证它能正确工作。下一部分将解决这个问题。
