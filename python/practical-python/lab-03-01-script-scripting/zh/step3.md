# 定义事物

名称在使用之前必须始终先进行定义。

```python
def square(x):
    return x*x

a = 42
b = a + 2     # 要求 `a` 已定义

z = square(b) # 要求 `square` 和 `b` 已定义
```

**顺序很重要**。你几乎总是将变量和函数的定义放在接近顶部的位置。
