# Create LineCollection using offsets

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

The fourth step is to create a LineCollection using offsets. We will be using the LineCollection to create curves with offsets. We will also be using the offset_transform to set the positions of the curves.
