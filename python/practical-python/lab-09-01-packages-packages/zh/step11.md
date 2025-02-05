# 练习9.1：创建一个简单的包

创建一个名为 `porty/` 的目录，并将上述所有Python文件放入其中。此外，创建一个空的 `__init__.py` 文件并将其放入该目录中。你应该有一个如下所示的文件目录：

    porty/
        __init__.py
        fileparse.py
        follow.py
        pcost.py
        portfolio.py
        report.py
        stock.py
        tableformat.py
        ticker.py
        typedproperty.py

删除你目录中存在的 `__pycache__` 文件。这包含之前预编译的Python模块。我们希望重新开始。

尝试导入一些包模块：

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

如果这些导入失败，请进入相应的文件并修复模块导入，以包含相对包的导入。例如，像 `import fileparse` 这样的语句可能会更改为以下内容：

    # report.py
    from. import fileparse

...

如果你有像 `from fileparse import parse_csv` 这样的语句，将代码更改为以下内容：

    # report.py
    from.fileparse import parse_csv

...
