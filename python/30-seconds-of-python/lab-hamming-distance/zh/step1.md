# 汉明距离

编写一个函数 `hamming_distance(a, b)`，该函数接受两个整数作为参数，并返回它们之间的汉明距离。该函数应执行以下步骤：

1. 使用异或运算符（`^`）找出两个数字之间的位差异。
2. 使用 `bin()` 将结果转换为二进制字符串。
3. 将字符串转换为列表，并使用 `str` 类的 `count()` 方法来计数并返回其中 `1` 的数量。

```python
def hamming_distance(a, b):
  return bin(a ^ b).count('1')
```

```python
hamming_distance(2, 3) # 1
```
