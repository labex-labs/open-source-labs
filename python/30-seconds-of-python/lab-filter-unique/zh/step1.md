# 过滤列表中的唯一值

编写一个名为 `filter_unique(lst)` 的 Python 函数，该函数接受一个列表作为参数，并返回一个只包含非唯一值的新列表。要解决这个问题，你可以按照以下步骤进行：

1. 使用 `collections.Counter` 获取列表中每个值的计数。
2. 使用列表推导式创建一个只包含非唯一值的列表。

你的函数应满足以下要求：

- 函数应接受一个列表作为参数。
- 函数应返回一个只包含非唯一值的新列表。
- 函数不应修改原始列表。
- 函数应区分大小写，即 'a' 和 'A' 被视为不同的值。

```python
def filter_unique(lst):
    # 在此处编写你的代码
```

```python
from collections import Counter

def filter_unique(lst):
  return [item for item, count in Counter(lst).items() if count > 1]
```

```python
filter_unique([1, 2, 2, 3, 4, 4, 5]) # [2, 4]
```
