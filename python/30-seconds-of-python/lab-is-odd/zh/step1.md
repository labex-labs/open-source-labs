# 检查一个数字是否为奇数

编写一个名为 `is_odd` 的函数，该函数接受一个整数作为参数，如果该数字为奇数，则返回 `True`，如果该数字为偶数，则返回 `False`。你的函数应执行以下步骤：

1. 使用取模 (`%`) 运算符检查该数字是偶数还是奇数。
2. 如果数字为奇数，则返回 `True`。如果数字为偶数，则返回 `False`。

```python
def is_odd(num):
  return num % 2!= 0
```

```python
is_odd(3) # True
```
