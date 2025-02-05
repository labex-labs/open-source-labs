# Create Insets with Arbitrary Positions

We can create insets with arbitrary positions by using the `bbox_to_anchor` parameter to specify a bounding box in data coordinates and using the `bbox_transform` parameter to specify the transform for the bounding box.

```python
# Create inset in data coordinates using ax.transData as transform
axins3 = inset_axes(ax2, width="100%", height="100%",
                    bbox_to_anchor=(1e-2, 2, 1e3, 3),
                    bbox_transform=ax2.transData, loc=2, borderpad=0)
```
