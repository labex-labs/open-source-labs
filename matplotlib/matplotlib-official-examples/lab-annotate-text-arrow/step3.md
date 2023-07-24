# Add a text arrow to indicate direction

To indicate the direction of the data, we'll add a text arrow using the `ax.text()` function and the `bbox` parameter with the `boxstyle` set to "rarrow".

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
