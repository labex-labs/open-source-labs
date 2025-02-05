# 生成器表达式与归约函数

生成器表达式对于将数据输入到诸如 `sum()`、`min()`、`max()`、`any()` 等函数中特别有用。使用之前的投资组合数据来试试一些例子。仔细观察，这些例子中缺少了使用列表推导式时出现的一些额外方括号（`[]`）。

```python
>>> from readport import read_portfolio
>>> portfolio = read_portfolio('portfolio.csv')
>>> sum(s['shares']*s['price'] for s in portfolio)
44671.15
>>> min(s['shares'] for s in portfolio)
50
>>> any(s['name'] == 'IBM' for s in portfolio)
True
>>> all(s['name'] == 'IBM' for s in portfolio)
False
>>> sum(s['shares'] for s in portfolio if s['name'] == 'IBM')
150
>>>
```

这里有一个在生成逗号分隔值时对生成器表达式的巧妙运用：

```python
>>> s = ('GOOG',100,490.10)
>>> ','.join(s)
... 注意它会失败...
>>> ','.join(str(x) for x in s)    # 这个可以
'GOOG,100,490.1'
>>>
```

上述例子中的语法需要一些时间来适应，但关键在于这些操作都不会创建一个完整填充的结果列表。这为你节省了大量内存。不过，你确实需要确保不要过度使用这种语法。
