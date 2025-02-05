# 练习 2.25：创建字典

还记得如果有键名和值的序列，`dict()` 函数可以轻松创建字典吗？让我们根据列标题来创建一个字典：

```python
>>> headers
['name', 'shares', 'price']
>>> converted
['AA', 100, 32.2]
>>> dict(zip(headers, converted))
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```

当然，如果你精通列表推导式，你可以使用字典推导式一步完成整个转换：

```python
>>> { name: func(val) for name, func, val in zip(headers, types, row) }
{'price': 32.2, 'name': 'AA', 'shares': 100}
>>>
```
