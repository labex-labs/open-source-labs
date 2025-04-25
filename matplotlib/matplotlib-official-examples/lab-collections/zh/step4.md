# 使用偏移量创建 LineCollection

```python
col = collections.LineCollection(
    [spiral], offsets=xyo, offset_transform=ax1.transData)
trans = fig.dpi_scale_trans + transforms.Affine2D().scale(1.0/72.0)
col.set_transform(trans)
col.set_color(colors)

ax1.add_collection(col, autolim=True)
ax1.autoscale_view()

ax1.set_title('LineCollection using offsets')
```

第四步是使用偏移量创建一个 LineCollection。我们将使用 LineCollection 来创建带有偏移量的曲线。我们还将使用 offset_transform 来设置曲线的位置。
