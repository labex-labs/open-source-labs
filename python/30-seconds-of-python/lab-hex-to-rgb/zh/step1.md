# 十六进制转 RGB

编写一个函数 `hex_to_rgb(hex_code)`，它接受一个十六进制颜色代码作为字符串，并返回一个对应其 RGB 分量的整数元组。该函数应执行以下步骤：

1. 使用列表推导式结合 `int()` 和列表切片表示法从十六进制字符串中获取 RGB 分量。
2. 使用 `tuple()` 将结果列表转换为元组。

```python
def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
```

```python
hex_to_rgb('FFA501') # (255, 165, 1)
```
