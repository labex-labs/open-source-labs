# 基于函数的列表交集

编写一个函数 `intersection_by(a, b, fn)`，它接受两个列表 `a` 和 `b`，以及一个函数 `fn`。该函数应在将提供的函数应用于两个列表的每个元素之后，返回两个列表中都存在的元素列表。

### 输入

- 两个列表 `a` 和 `b` (1 <= `a` 的长度, `b` 的长度 <= 1000)
- 一个函数 `fn`，它接受一个参数并返回一个值

### 输出

- 在将提供的函数应用于两个列表的每个元素之后，两个列表中都存在的元素列表。

```python
def intersection_by(a, b, fn):
  _b = set(map(fn, b))
  return [item for item in a if fn(item) in _b]
```

```python
from math import floor

intersection_by([2.1, 1.2], [2.3, 3.4], floor) # [2.1]
```
