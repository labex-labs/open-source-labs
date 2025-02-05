# 绘制数据

我们将在同一图表上绘制三个数据集：密度、温度和速度。我们将使用 `plot()` 函数来绘制数据。

```python
p1, = host.plot([0, 1, 2], [0, 1, 2], label="Density")
p2, = par1.plot([0, 1, 2], [0, 3, 2], label="Temperature")
p3, = par2.plot([0, 1, 2], [50, 30, 15], label="Velocity")
```
