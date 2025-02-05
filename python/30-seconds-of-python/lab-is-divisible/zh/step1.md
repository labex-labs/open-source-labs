# 数字可整除性

编写一个函数 `is_divisible(dividend, divisor)`，它接受两个整数作为参数，如果 `dividend` 能被 `divisor` 整除，则返回 `True`，否则返回 `False`。

```python
def is_divisible(dividend, divisor):
  return dividend % divisor == 0
```

```python
is_divisible(6, 3) # True
```
