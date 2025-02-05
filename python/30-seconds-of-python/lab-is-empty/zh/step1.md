# 集合为空

编写一个名为 `is_empty(val)` 的 Python 函数，该函数接受一个值作为参数，如果该值是空序列或集合，则返回 `True`，否则返回 `False`。

要检查一个序列或集合是否为空，可以使用 `not` 运算符来测试所提供序列或集合的真值。如果序列或集合为空，`not` 运算符将返回 `True`。

你的函数应该能够处理以下类型的序列和集合：

- 列表（Lists）
- 元组（Tuples）
- 集合（Sets）
- 字典（Dictionaries）
- 字符串（Strings）
- 范围（Ranges）

```python
def is_empty(val):
  return not val
```

```python
is_empty([]) # True
is_empty({}) # True
is_empty('') # True
is_empty(set()) # True
is_empty(range(0)) # True
is_empty([1, 2]) # False
is_empty({ 'a': 1, 'b': 2 }) # False
is_empty('text') # False
is_empty(set([1, 2])) # False
is_empty(range(2)) # False
```
