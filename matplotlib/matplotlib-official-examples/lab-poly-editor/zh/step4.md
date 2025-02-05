# 创建多边形

我们需要使用 `Polygon` 类创建一个我们将进行编辑的多边形。

```python
theta = np.arange(0, 2*np.pi, 0.1)
r = 1.5

xs = r * np.cos(theta)
ys = r * np.sin(theta)

poly = Polygon(np.column_stack([xs, ys]), animated=True)
```
