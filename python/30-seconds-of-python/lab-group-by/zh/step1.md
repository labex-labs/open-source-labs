# 对列表元素进行分组

编写一个函数 `group_by(lst, fn)`，它接受一个列表 `lst` 和一个函数 `fn` 作为参数，并返回一个字典，其中键是将 `fn` 应用于 `lst` 元素的结果，值是 `lst` 中那些在应用 `fn` 时产生相应键的元素列表。

例如，如果我们有一个数字列表 `[6.1, 4.2, 6.3]`，并且我们想按它们的整数部分进行分组，我们可以使用 `math` 模块中的 `floor` 函数作为分组函数。预期输出将是 `{4: [4.2], 6: [6.1, 6.3]}`。

```python
from collections import defaultdict

def group_by(lst, fn):
  d = defaultdict(list)
  for el in lst:
    d[fn(el)].append(el)
  return dict(d)
```

```python
from math import floor

group_by([6.1, 4.2, 6.3], floor) # {4: [4.2], 6: [6.1, 6.3]}
group_by(['one', 'two', 'three'], len) # {3: ['one', 'two'], 5: ['three']}
```
