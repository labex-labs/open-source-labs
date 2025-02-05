# 练习2.20：序列归约

使用一条Python语句计算投资组合的总成本。

```python
>>> portfolio = read_portfolio('portfolio.csv')
>>> cost = sum([ s['shares'] * s['price'] for s in portfolio ])
>>> cost
44671.15
>>>
```

完成上述操作后，展示如何使用一条语句计算投资组合的当前价值。

```python
>>> value = sum([ s['shares'] * prices[s['name']] for s in portfolio ])
>>> value
28686.1
>>>
```

上述两个操作都是映射归约的示例。列表推导式在列表上映射一个操作。

```python
>>> [ s['shares'] * s['price'] for s in portfolio ]
[3220.0000000000005, 4555.0, 12516.0, 10246.0, 3835.1499999999996, 3254.9999999999995, 7044.0]
>>>
```

然后 `sum()` 函数对结果进行归约：

```python
>>> sum(_)
44671.15
>>>
```

有了这些知识，你现在就可以准备去创办一家大数据初创公司了。
