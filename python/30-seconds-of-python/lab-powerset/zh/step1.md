# 幂集

编写一个名为 `powerset(iterable)` 的Python函数，该函数接受一个可迭代对象作为参数，并返回该可迭代对象的幂集。该函数应遵循以下步骤：

1. 将给定值转换为列表。
2. 使用 `range()` 和 `itertools.combinations()` 创建一个生成器，该生成器返回所有子集。
3. 使用 `itertools.chain.from_iterable()` 和 `list()` 来消耗生成器并返回一个列表。

```python
from itertools import chain, combinations

def powerset(iterable):
  s = list(iterable)
  return list(chain.from_iterable(combinations(s, r) for r in range(len(s)+1)))
```

```python
powerset([1, 2]) # [(), (1,), (2,), (1, 2)]
```
