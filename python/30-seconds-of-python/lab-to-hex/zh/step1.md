# 十进制数转十六进制

编写一个函数 `to_hex(dec)`，它接受一个十进制数作为参数，并返回其十六进制表示形式。你的函数应执行以下步骤：

1. 使用 `hex()` 将十进制数转换为其十六进制等效值。
2. 返回十六进制表示形式。

```python
def to_hex(dec):
  return hex(dec)
```

```python
to_hex(41) # 0x29
to_hex(332) # 0x14c
```
