# 创建绘图

我们将使用 Matplotlib 创建一个绘图。我们将使用 xdata 和 ydata 创建 `DataDisplayDownsampler` 类的一个实例 `d`。我们将使用 subplots 函数创建一个图形和一个坐标轴。我们将连接线条并将自动缩放设置为 False。我们将连接以更改视图限制，设置 x 轴限制并显示绘图。

```python
d = DataDisplayDownsampler(xdata, ydata)
fig, ax = plt.subplots()
d.line, = ax.plot(xdata, ydata, 'o-')
ax.set_autoscale_on(False)
ax.callbacks.connect('xlim_changed', d.update)
ax.set_xlim(16, 365)
plt.show()
```
