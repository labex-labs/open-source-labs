# 向绘图中添加数据

我们使用 `plot` 方法向绘图中添加数据。我们向绘图中添加三条线，每条线使用不同的 y 轴。

```python
p1, = ax.plot([0, 1, 2], [0, 1, 2], "C0", label="Density")
p2, = twin1.plot([0, 1, 2], [0, 3, 2], "C1", label="Temperature")
p3, = twin2.plot([0, 1, 2], [50, 30, 15], "C2", label="Velocity")
```
