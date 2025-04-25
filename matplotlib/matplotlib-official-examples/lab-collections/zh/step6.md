# 使用偏移量创建 RegularPolyCollection

```python
col = collections.RegularPolyCollection(
    7, sizes=np.abs(xx) * 10.0, offsets=xyo, offset_transform=ax3.transData)
trans = transforms.Affine2D().scale(fig.dpi / 72.0)
col.set_transform(trans)
col.set_color(colors)

ax3.add_collection(col, autolim=True)
ax3.autoscale_view()

ax3.set_title('RegularPolyCollection using offsets')
```

第六步是使用偏移量创建一个 RegularPolyCollection。我们将使用 RegularPolyCollection 来创建带有偏移量的正多边形。我们还将使用 offset_transform 来设置多边形的位置。
