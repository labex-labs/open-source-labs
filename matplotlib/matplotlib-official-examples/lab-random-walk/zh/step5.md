# 创建三维绘图

我们使用 `matplotlib` 创建一个三维绘图。我们为每个随机游走在绘图中添加一条空线条。我们将 x、y 和 z 轴的范围设置在 0 到 1 之间。

```python
# 将三维轴附加到图形
fig = plt.figure()
ax = fig.add_subplot(projection="3d")

# 最初创建没有数据的线条
lines = [ax.plot([], [], [])[0] for _ in walks]

# 设置轴属性
ax.set(xlim3d=(0, 1), xlabel='X')
ax.set(ylim3d=(0, 1), ylabel='Y')
ax.set(zlim3d=(0, 1), zlabel='Z')
```
