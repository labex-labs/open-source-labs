# 用值初始化列表

编写一个函数 `initialize_list_with_values(n, val=0)`，该函数接受两个参数：

- `n`（整数），表示要创建的列表的长度。
- `val`（整数），表示用于填充列表的值。如果未提供 `val`，则应使用默认值 `0`。

该函数应返回一个长度为 `n` 的列表，其中填充了指定的值。

```python
def initialize_list_with_values(n, val = 0):
  return [val for x in range(n)]
```

```python
initialize_list_with_values(5, 2) # [2, 2, 2, 2, 2]
```
