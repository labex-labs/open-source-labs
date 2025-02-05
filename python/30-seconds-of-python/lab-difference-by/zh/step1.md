# 基于函数的列表差异

创建一个名为 `difference_by(a, b, fn)` 的函数，该函数接受三个参数：

- `a`：一个元素列表
- `b`：一个元素列表
- `fn`：一个将应用于两个列表中每个元素的函数

该函数应返回列表 `a` 中存在但列表 `b` 中不存在的元素列表，前提是已将提供的函数 `fn` 应用于两个列表中的每个元素。

要解决此问题，你可以按以下步骤操作：

1. 使用 `map()` 将 `fn` 应用于 `b` 中的每个元素，创建一个集合。
2. 对 `a` 使用列表推导式并结合 `fn`，只保留不在先前创建的集合 `_b` 中的值。

```python
def difference_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) not in _b]
```

```python
from math import floor

difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2]
difference_by([{ 'x': 2 }, { 'x': 1 }], [{ 'x': 1 }], lambda v : v['x'])
# [ { x: 2 } ]
```
