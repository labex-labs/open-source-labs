# 练习7.5：按字段排序

尝试以下语句，这些语句按股票名称对投资组合数据进行字母排序。

```python
>>> def stock_name(s):
       return s.name

>>> portfolio.sort(key=stock_name)
>>> for s in portfolio:
           print(s)

... 检查结果...
>>>
```

在这部分中，`stock_name()` 函数从 `portfolio` 列表中的单个条目中提取股票名称。`sort()` 使用此函数的结果进行比较。
