# 值频率

编写一个名为 `value_frequencies(lst)` 的 Python 函数，该函数接受一个列表作为参数，并返回一个字典，其中列表中的唯一值作为键，它们的频率作为值。

要解决这个问题，你可以按照以下步骤进行：

1. 创建一个空字典来存储每个唯一元素的频率。
2. 遍历列表，并使用 `collections.defaultdict` 来存储每个唯一元素的频率。
3. 使用 `dict()` 返回一个字典，其中列表中的唯一元素作为键，它们的频率作为值。

你的函数应该返回包含唯一值及其频率的字典。

```python
from collections import defaultdict

def frequencies(lst):
  freq = defaultdict(int)
  for val in lst:
    freq[val] += 1
  return dict(freq)
```

```python
frequencies(['a', 'b', 'a', 'c', 'a', 'a', 'b']) # { 'a': 4, 'b': 2, 'c': 1 }
```
