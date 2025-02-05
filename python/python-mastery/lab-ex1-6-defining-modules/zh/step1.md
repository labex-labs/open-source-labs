# 使用 import 语句

在之前的练习中，你编写了两个程序 `pcost.py` 和 `stock.py`。使用 `import` 语句加载这些程序并使用它们的功能：

```python
>>> import pcost
44671.15
>>> pcost.portfolio_cost('portfolio2.dat')
19908.75
>>> from stock import Stock
>>> s = Stock('GOOG', 100, 490.10)
>>> s.name
'GOOG'
>>> s.cost()
49010.0
>>>
```

如果你无法使上述语句生效，可能是你将程序放在了一个奇怪的目录中。确保你在与文件相同的目录中运行 Python，或者该目录包含在 `sys.path` 中。
