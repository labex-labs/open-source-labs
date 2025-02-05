# 创建截断斜线

最后，我们将创建截断斜线。我们将在坐标轴坐标系中创建线条对象，并使用 `ax1.transAxes` 和 `ax2.transAxes` 将它们转换为每个子图的坐标系。我们将使用 `ax1.plot` 和 `ax2.plot` 来绘制这些线条。我们还将使用 `marker` 来指定标记样式，`markersize` 来设置标记的大小，`linestyle` 来设置线条的样式，`color` 来设置线条的颜色，`mec` 来设置标记边缘的颜色，以及 `mew` 来设置标记边缘的宽度。

```python
d =.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
