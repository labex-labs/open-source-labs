# 一个上下文管理器

在练习3.5中，你让用户能够生成格式良好的表格。例如：

```python
>>> from tableformat import create_formatter
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

这段代码的一个问题是，所有表格都打印到标准输出（`sys.stdout`）。假设你想将输出重定向到一个文件或其他位置。从整体来看，你可能会修改所有的表格格式化代码以允许使用不同的输出文件。然而，在紧急情况下，你也可以使用上下文管理器来解决这个问题。

定义以下上下文管理器：

```python
>>> import sys
>>> class redirect_stdout:
        def __init__(self, out_file):
            self.out_file = out_file
        def __enter__(self):
            self.stdout = sys.stdout
            sys.stdout = self.out_file
            return self.out_file
        def __exit__(self, ty, val, tb):
            sys.stdout = self.stdout
```

这个上下文管理器的工作方式是对 `sys.stdout` 进行临时补丁，使所有输出重定向到另一个文件。在退出时，补丁会被撤销。试试看：

```python
>>> from tableformat import create_formatter
>>> formatter = create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
        tableformat.print_table(portfolio, ['name','shares','price'], formatter)
        file.close()

>>> # 检查文件
>>> print(open('out.txt').read())
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
