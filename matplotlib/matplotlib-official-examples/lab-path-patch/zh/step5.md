# 绘制控制点和连接线

在这一步中，我们使用轴对象的 `plot` 方法绘制路径的控制点和连接线。

```python
x, y = zip(*path.vertices)
line, = ax.plot(x, y, 'go-')
```
