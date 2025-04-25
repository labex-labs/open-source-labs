# 练习 7.6：使用 lambda 按字段排序

尝试使用 `lambda` 表达式按股票数量对投资组合进行排序：

```python
>>> portfolio.sort(key=lambda s: s.shares)
>>> for s in portfolio:
        print(s)

... 检查结果...
>>>
```

尝试按每只股票的价格对投资组合进行排序

```python
>>> portfolio.sort(key=lambda s: s.price)
>>> for s in portfolio:
        print(s)

... 检查结果...
>>>
```

注意：`lambda` 是一个有用的捷径，因为它允许你直接在对 `sort()` 的调用中定义一个特殊的处理函数，而不必先定义一个单独的函数。
