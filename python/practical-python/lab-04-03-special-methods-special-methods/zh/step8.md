# 练习 4.9：改进对象打印输出

修改你在 `stock.py` 中定义的 `Stock` 对象，使 `__repr__()` 方法产生更有用的输出。例如：

```python
>>> goog = stock.Stock('GOOG', 100, 490.1)
>>> goog
Stock('GOOG', 100, 490.1)
>>>
```

看看在你进行这些更改后，读取股票投资组合并查看结果列表时会发生什么。例如：

```python
>>> import report
>>> portfolio = report.read_portfolio('portfolio.csv')
>>> portfolio
... 查看输出结果...
>>>
```
