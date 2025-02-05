# 将列表拆分成多个块

编写一个函数 `chunk(lst, size)`，它接受一个列表 `lst` 和一个正整数 `size` 作为参数，并返回一个由较小列表组成的列表，每个较小列表的最大大小为 `size`。如果 `lst` 的长度不能被 `size` 整除，则返回列表中的最后一个列表应包含剩余的元素。

```python
from math import ceil

def chunk(lst, size):
  return list(
    map(lambda x: lst[x * size:x * size + size],
      list(range(ceil(len(lst) / size)))))
```

```python
chunk([1, 2, 3, 4, 5], 2) # [[1, 2], [3, 4], [5]]
```
