# 合并字典值

编写一个函数 `combine_values(*dicts)`，它接受两个或更多字典作为参数，并返回一个新字典，该字典合并了输入字典的值。该函数应执行以下步骤：

1. 创建一个新的 `collections.defaultdict`，其中每个键的默认值为列表。
2. 遍历输入字典，对于每个字典：
   - 遍历字典的键。
   - 将键的值追加到 `defaultdict` 中该键的值列表中。
3. 使用 `dict()` 函数将 `defaultdict` 转换为常规字典。
4. 返回结果字典。

该函数应具有以下签名：

```python
def combine_values(*dicts):
    pass
```

```python
from collections import defaultdict

def combine_values(*dicts):
  res = defaultdict(list)
  for d in dicts:
    for key in d:
      res[key].append(d[key])
  return dict(res)
```

```python
d1 = {'a': 1, 'b': 'foo', 'c': 400}
d2 = {'a': 3, 'b': 200, 'd': 400}

combine_values(d1, d2) # {'a': [1, 3], 'b': ['foo', 200], 'c': [400], 'd': [400]}
```
