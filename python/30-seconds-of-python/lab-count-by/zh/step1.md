# 统计分组后的元素

编写一个函数 `count_by(lst, fn = lambda x: x)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数。该函数应根据给定的函数对列表中的元素进行分组，并返回一个字典，其中包含每个组中元素的计数。

要解决这个问题，你可以按照以下步骤进行：

1. 使用 `collections.defaultdict` 初始化一个字典。
2. 使用 `map()` 将给定的函数应用于列表中的每个元素。
3. 遍历映射后的值，并增加字典中每个元素的计数。

该函数应返回结果字典。

```python
from collections import defaultdict

def count_by(lst, fn = lambda x: x):
  count = defaultdict(int)
  for val in map(fn, lst):
    count[val] += 1
  return dict(count)
```

```python
from math import floor

count_by([6.1, 4.2, 6.3], floor) # {6: 2, 4: 1}
count_by(['one', 'two', 'three'], len) # {3: 2, 5: 1}
```
