# 使其合理

对于框架构建者来说，使用混入类是一种有用的工具，可以减少需要编写的代码量。然而，强迫用户记住如何正确组合类以及使用多重继承可能会让他们抓狂。在练习3.5中，你编写了一个函数`create_formatter()`，它使创建自定义格式化器变得更容易。采用该函数并对其进行扩展，使其理解一些与混入类相关的可选参数。例如：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('csv', column_formats=['"%s"','%d','%0.2f'])
>>> print_table(portfolio, ['name','shares','price'], formatter)
name,shares,price
"AA",100,32.20
"IBM",50,91.10
"CAT",150,83.44
"MSFT",200,51.23
"GE",95,40.37
"MSFT",50,65.10
"IBM",100,70.44

>>> formatter = create_formatter('text', upper_headers=True)
>>> print_table(portfolio, ['name','shares','price'], formatter)
      NAME     SHARES      PRICE
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

在底层，`create_formatter()`函数将正确地组合类并返回一个合适的`TableFormatter`实例。
