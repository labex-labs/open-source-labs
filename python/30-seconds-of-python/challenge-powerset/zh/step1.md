# 幂集挑战

## 问题

编写一个名为 `powerset(iterable)` 的 Python 函数，该函数接受一个可迭代对象作为参数，并返回该可迭代对象的幂集。该函数应遵循以下步骤：

1. 将给定的值转换为列表。
2. 使用 `range()` 和 `itertools.combinations()` 创建一个生成器，该生成器返回所有子集。
3. 使用 `itertools.chain.from_iterable()` 和 `list()` 来消耗生成器并返回一个列表。

## 示例

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
