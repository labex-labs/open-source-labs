# 创建图形和坐标轴

在这一步中，你将为绘图创建图形和坐标轴。你还将调整坐标轴的位置，以便为滑块留出空间。

```python
fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.25)
l, = ax.plot(t, s, lw=2)

ax_freq = fig.add_axes([0.25, 0.1, 0.65, 0.03])
ax_amp = fig.add_axes([0.25, 0.15, 0.65, 0.03])
```
