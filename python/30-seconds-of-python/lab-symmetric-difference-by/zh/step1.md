# 基于函数的对称差

编写一个函数 `symmetric_difference_by(a, b, fn)`，它接受两个列表 `a` 和 `b` 以及一个函数 `fn`。该函数应返回一个新列表，其中包含在对两个原始列表的每个元素都应用了提供的函数之后，在两个原始列表中的任意一个中出现，但不在两个列表中都出现的所有元素。

要解决这个问题，你可以按照以下步骤进行：

1. 通过对每个列表中的每个元素应用 `fn` 创建一个 `set`。
2. 对每个列表使用列表推导式并结合 `fn`，只保留不在另一个列表先前创建的集合中的值。
3. 连接步骤 2 中获得的两个列表。

该函数应具有以下参数：

- `a`：一个元素列表
- `b`：一个元素列表
- `fn`：一个接受一个元素并返回一个新值的函数

该函数应返回一个新列表，其中包含在对两个原始列表的每个元素都应用了提供的函数之后，在两个原始列表中的任意一个中出现，但不在两个列表中都出现的所有元素。

```python
def symmetric_difference_by(a, b, fn):
  (_a, _b) = (set(map(fn, a)), set(map(fn, b)))
  return [item for item in a if fn(item) not in _b] + [item
          for item in b if fn(item) not in _a]
```

```python
from math import floor

symmetric_difference_by([2.1, 1.2], [2.3, 3.4], floor) # [1.2, 3.4]
```
