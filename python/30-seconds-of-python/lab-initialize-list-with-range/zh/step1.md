# 使用范围初始化列表

编写一个函数 `initialize_list_with_range(end, start=0, step=1)`，该函数初始化一个包含指定范围内数字的列表，其中 `start` 和 `end` 包含在范围内，它们的公差为 `step`。

该函数应返回一个长度合适的列表，其中填充了给定范围内的所需值。

### 输入

- `end`（整数） - 范围的结束值（包含）。
- `start`（整数，可选） - 范围的起始值（包含）。默认值为 0。
- `step`（整数，可选） - 范围内每个数字之间的公差。默认值为 1。

### 输出

- 一个包含指定范围内数字的列表。

```python
def initialize_list_with_range(end, start = 0, step = 1):
  return list(range(start, end + 1, step))
```

```python
initialize_list_with_range(5) # [0, 1, 2, 3, 4, 5]
initialize_list_with_range(7, 3) # [3, 4, 5, 6, 7]
initialize_list_with_range(9, 0, 2) # [0, 2, 4, 6, 8]
```
