# 生成数据

接下来，我们需要生成一些要绘制的数据。在这个例子中，我们将创建三个数组：一个用于 x 轴值，一个用于第一个图中的 y 轴值，另一个用于第三个图中的 y 轴值。

```python
dt = 0.01
x = np.arange(-50.0, 50.0, dt)
y1 = np.arange(0, 100.0, dt)
y3 = np.sin(x / 3.0)
```
