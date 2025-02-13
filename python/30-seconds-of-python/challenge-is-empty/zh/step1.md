# 集合为空

## 问题

编写一个名为 `is_empty(val)` 的 Python 函数，该函数将一个值作为参数，如果该值是空序列或集合，则返回 `True`，否则返回 `False`。

要检查一个序列或集合是否为空，可以使用 `not` 运算符来测试所提供序列或集合的真值。如果序列或集合为空，`not` 运算符将返回 `True`。

你的函数应该能够处理以下类型的序列和集合：

- 列表
- 元组
- 集合
- 字典
- 字符串
- 范围

## 示例

```python
assert is_empty([]) == True
assert is_empty({}) == True
assert is_empty('') == True
assert is_empty(set()) == True
assert is_empty(range(0)) == True
assert is_empty([1, 2]) == False
assert is_empty({'a': 1, 'b': 2}) == False
assert is_empty('text') == False
assert is_empty(set([1, 2])) == False
assert is_empty(range(2)) == False
```
