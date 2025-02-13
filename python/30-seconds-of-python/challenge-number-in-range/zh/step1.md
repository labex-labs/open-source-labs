# 在范围内的数字

## 问题

编写一个函数 `in_range(n, start, end = 0)`，它接受三个参数：

- `n`：要检查是否在范围内的数字
- `start`：范围的起始值
- `end`：范围的结束值（可选，默认值为 0）

如果给定的数字 `n` 在指定范围内，函数应返回 `True`，否则返回 `False`。如果未指定 `end` 参数，则范围被视为从 `0` 到 `start`。

## 示例

```python
in_range(3, 2, 5) # True
in_range(3, 4) # True
in_range(2, 3, 5) # False
in_range(3, 2) # False
```
