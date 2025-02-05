# 正方形的联合/边缘绘图

在联合数据绘图旁边展示边缘分布可能是很有用的。以下代码创建了一个正方形绘图，其中边缘坐标轴的框体纵横比等于网格布局（gridspec）的宽度和高度比例。这确保了所有坐标轴能完美对齐，而不受图形大小的影响。

```python
fig5, axs = plt.subplots(2, 2, sharex="col", sharey="row",
                         gridspec_kw=dict(height_ratios=[1, 3],
                                          width_ratios=[3, 1]))
axs[0, 1].set_visible(False)
axs[0, 0].set_box_aspect(1/3)
axs[1, 0].set_box_aspect(1)
axs[1, 1].set_box_aspect(3/1)

np.random.seed(19680801)  # Fixing random state for reproducibility
x, y = np.random.randn(2, 400) * [[.5], [180]]
axs[1, 0].scatter(x, y)
axs[0, 0].hist(x)
axs[1, 1].hist(y, orientation="horizontal")

plt.show()
```
