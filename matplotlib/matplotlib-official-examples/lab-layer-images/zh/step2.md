# 定义 x 和 y 变量

定义 x 和 y 变量以创建网格。

```python
dx, dy = 0.05, 0.05
x = np.arange(-3.0, 3.0, dx)
y = np.arange(-3.0, 3.0, dy)
X, Y = np.meshgrid(x, y)
```
