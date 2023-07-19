# Create PolyCollection using offsets

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

The fifth step is to create a PolyCollection using offsets. We will be using the PolyCollection to fill the curves with colors. We will also be using the offset_transform to set the positions of the curves.
