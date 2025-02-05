# Create RegularPolyCollection using offsets

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

The sixth step is to create a RegularPolyCollection using offsets. We will be using the RegularPolyCollection to create regular polygons with offsets. We will also be using the offset_transform to set the positions of the polygons.
