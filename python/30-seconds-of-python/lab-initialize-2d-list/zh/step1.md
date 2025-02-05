# 初始化二维列表

编写一个函数 `initialize_2d_list(w, h, val=None)`，用于初始化一个具有给定宽度、高度和值的二维列表。该函数应返回一个包含 `h` 行的列表，其中每行是一个长度为 `w` 的列表，并用 `val` 进行初始化。如果未提供 `val`，则默认值应为 `None`。

```python
def initialize_2d_list(w, h, val = None):
  return [[val for x in range(w)] for y in range(h)]
```

```python
initialize_2d_list(2, 2, 0) # [[0, 0], [0, 0]]
```
