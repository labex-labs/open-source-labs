# 共享坐标轴

默认情况下，每个 `Axes` 都是独立缩放的。要对齐子图的水平或垂直轴，我们可以使用 `sharex` 或 `sharey` 参数。

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(x, y)
ax2.plot(x + 1, -y)
```
