# 设置绘图

现在，我们需要设置绘图。我们将使用 Matplotlib 的 `subplots()` 函数创建一个图形和一个坐标轴对象。我们还将创建一个线条对象来表示正弦波。

```python
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []
```
