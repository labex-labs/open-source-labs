# 钳位数字

编写一个函数 `clamp_number(num, a, b)`，它接受三个参数：

- `num`（整数或浮点数）：要钳位的数字
- `a`（整数或浮点数）：范围的下限
- `b`（整数或浮点数）：范围的上限

该函数应将 `num` 钳位在边界值指定的包含范围内。如果 `num` 在范围 (`a`, `b`) 内，则返回 `num`。否则，返回该范围内最接近的数字。

```python
def clamp_number(num, a, b):
  return max(min(num, max(a, b)), min(a, b))
```

```python
clamp_number(2, 3, 5) # 3
clamp_number(1, -1, -5) # -1
```
