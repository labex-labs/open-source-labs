# 使用偏移量创建PolyCollection

```python
col = collections.PolyCollection(
    [spiral], offsets=xyo, offset_transform=ax2.transData)
trans = transforms.Affine2D().scale(fig.dpi/72.0)
col.set_transform(trans)
col.set_color(colors)

ax2.add_collection(col, autolim=True)
ax2.autoscale_view()

ax2.set_title('PolyCollection using offsets')
```

第五步是使用偏移量创建一个PolyCollection。我们将使用PolyCollection为曲线填充颜色。我们还将使用offset_transform来设置曲线的位置。
