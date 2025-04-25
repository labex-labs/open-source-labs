# 练习 3.11：模块导入

在第 3 节中，我们创建了一个通用函数 `parse_csv()` 来解析 CSV 数据文件的内容。

现在，我们将看看如何在其他程序中使用该函数。首先，在一个新的 shell 窗口中开始。导航到你存放所有文件的文件夹。我们将导入这些文件。

启动 Python 交互模式。

```shell
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

完成上述操作后，尝试导入一些你之前编写的程序。你应该会看到和之前完全一样的输出。需要强调的是，导入一个模块会运行其代码。

```python
>>> import bounce
... 查看输出...
>>> import mortgage
... 查看输出...
>>> import report
... 查看输出...
>>>
```

如果这些都不起作用，你可能在错误的目录中运行 Python。现在，尝试导入你的 `fileparse` 模块并获取相关帮助。

```python
>>> import fileparse
>>> help(fileparse)
... 查看输出...
>>> dir(fileparse)
... 查看输出...
>>>
```

尝试使用该模块读取一些数据：

```python
>>> portfolio = fileparse.parse_csv('/home/labex/project/portfolio.csv',select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... 查看输出...
>>> pricelist = fileparse.parse_csv('/home/labex/project/prices.csv',types=[str,float], has_headers=False)
>>> pricelist
... 查看输出...
>>> prices = dict(pricelist)
>>> prices
... 查看输出...
>>> prices['IBM']
106.28
>>>
```

尝试导入一个函数，这样你就不需要包含模块名：

```python
>>> from fileparse import parse_csv
>>> portfolio = parse_csv('/home/labex/project/portfolio.csv', select=['name','shares','price'], types=[str,int,float])
>>> portfolio
... 查看输出...
>>>
```
