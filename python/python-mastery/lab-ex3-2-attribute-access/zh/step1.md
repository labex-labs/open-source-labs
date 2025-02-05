# 三种操作

整个 Python 对象系统仅由三种核心操作组成：获取、设置和删除属性。通常，这些操作通过点号（.）来访问，如下所示：

```python
>>> s = Stock('GOOG', 100, 490.1)
>>> s.name    # 获取
'GOOG'
>>> s.shares = 50    # 设置
>>> del s.shares     # 删除
>>>
```

这三种操作也可以作为函数使用。例如：

```python
>>> getattr(s, 'name')            # 等同于 s.name
'GOOG'
>>> setattr(s,'shares', 50)      # 等同于 s.shares = 50
>>> delattr(s,'shares')          # 等同于 del s.shares
>>>
```

另一个函数 `hasattr()` 可用于检查对象是否存在某个属性：

```python
>>> hasattr(s, 'name')
True
>>> hasattr(s, 'blah')
False
>>>
```
