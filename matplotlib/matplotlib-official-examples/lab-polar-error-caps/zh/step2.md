# 创建数据

在这一步中，我们将为误差线图创建数据。我们将使用 NumPy 创建一个 theta 值数组和一个相应半径值数组。

```python
theta = np.arange(0, 2 * np.pi, np.pi / 4)
r = theta / np.pi / 2 + 0.5
```
