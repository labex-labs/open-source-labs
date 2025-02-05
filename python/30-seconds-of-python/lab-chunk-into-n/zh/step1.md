# 将列表拆分为 N 个块

编写一个名为 `chunk_into_n(lst, n)` 的 Python 函数，该函数接受一个列表 `lst` 和一个整数 `n` 作为输入，并返回一个由 `n` 个较小列表组成的列表，每个较小列表包含原始列表中数量相等的元素。如果原始列表不能均匀地拆分为 `n` 个较小列表，则最后一个块应包含剩余的元素。

要解决此问题，你可以按以下步骤操作：

1. 通过将原始列表的长度除以 `n` 并使用 `math.ceil()` 函数向上取整到最接近的整数来计算每个块的大小。
2. 使用 `list()` 和 `range()` 函数创建一个大小为 `n` 的新列表。
3. 使用 `map()` 函数将新列表的每个元素映射到原始列表中长度为 `size` 的一个块。
4. 返回较小列表的列表。

你的函数应具有以下签名：

```python
def chunk_into_n(lst: list, n: int) -> list:
```

```python
from math import ceil

def chunk_into_n(lst, n):
  size = ceil(len(lst) / n)
  return list(
    map(lambda x: lst[x * size:x * size + size],
    list(range(n)))
  )
```

```python
chunk_into_n([1, 2, 3, 4, 5, 6, 7], 4) # [[1, 2], [3, 4], [5, 6], [7]]
```
