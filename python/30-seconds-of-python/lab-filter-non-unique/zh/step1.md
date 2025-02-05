# 过滤列表中的非唯一值

编写一个名为 `filter_non_unique(lst)` 的 Python 函数，该函数接受一个列表作为参数，并返回一个只包含唯一值的新列表。要解决这个问题，你可以按照以下步骤进行：

1. 使用 `collections.Counter` 方法获取列表中每个值的计数。
2. 使用列表推导式创建一个只包含唯一值的列表。

```python
from collections import Counter

def filter_non_unique(lst):
  return [item for item, count in Counter(lst).items() if count == 1]
```

```python
filter_non_unique([1, 2, 2, 3, 4, 4, 5]) # [1, 3, 5]
```
