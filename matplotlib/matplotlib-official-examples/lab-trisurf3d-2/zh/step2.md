# 创建网格

我们在参数化变量 `u` 和 `v` 的空间中创建一个网格。这是通过使用 `np.meshgrid()` 函数来创建 `u` 和 `v` 点的网格来完成的。

```python
u = np.linspace(0, 2.0 * np.pi, endpoint=True, num=50)
v = np.linspace(-0.5, 0.5, endpoint=True, num=10)
u, v = np.meshgrid(u, v)
u, v = u.flatten(), v.flatten()
```
