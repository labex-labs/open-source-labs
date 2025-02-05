# 阶乘

编写一个函数 `factorial(num)`，它接受一个非负整数 `num` 作为参数，并返回其阶乘。该函数应使用递归计算阶乘。如果 `num` 小于或等于 `1`，则返回 `1`。否则，返回 `num` 与 `num - 1` 的阶乘的乘积。如果 `num` 是负数或浮点数，该函数应抛出异常。

```python
def factorial(num):
  if not ((num >= 0) and (num % 1 == 0)):
    raise Exception("Number can't be floating point or negative.")
  return 1 if num == 0 else num * factorial(num - 1)
```

```python
factorial(6) # 720
```
