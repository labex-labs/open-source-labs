# 创建图形和坐标轴

我们需要为条形码创建图形和坐标轴。我们将把图形大小设置为数据点数量的倍数，并关闭所有坐标轴。

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
