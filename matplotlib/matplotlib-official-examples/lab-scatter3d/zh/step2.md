# 设置数据

我们将使用 NumPy 库生成两组具有随机值的数据。一组将表示 x 和 y 坐标，另一组将表示 z 坐标。

```python
def randrange(n, vmin, vmax):
    """
    辅助函数，用于生成形状为 (n, ) 的随机数数组，
    其中每个数在 Uniform(vmin, vmax) 范围内分布。
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

n = 100

for m, zlow, zhigh in [('o', -50, -25), ('^', -30, -5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 100)
    zs = randrange(n, zlow, zhigh)
```
