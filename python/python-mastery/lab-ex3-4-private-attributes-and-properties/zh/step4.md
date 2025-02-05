# 添加 `__slots__`

修改你的新 `Stock` 类以使用 `__slots__`。你会发现你必须使用与之前不同的一组属性名 —— 具体来说，你必须列出私有属性名（例如，如果一个特性在 `_shares` 属性中存储值，那么这就是你在 `__slots__` 中列出的名称）。验证该类仍然可以正常工作，并且你不能再添加新的属性。

```python
>>> s = Stock('GOOG', 100, 490.10)
>>> s.spam = 42
Traceback (最近一次调用最后):
  File "<stdin>", line 1, in <module>
AttributeError: 'Stock' 对象没有属性'spam'
>>>
```
