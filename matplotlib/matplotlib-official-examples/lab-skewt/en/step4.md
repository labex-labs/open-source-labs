# Define SkewSpine Class

The SkewSpine class calculates the separate data range of the upper X-axis and draws the spine there. It also provides this range to the X-axis artist for ticking and gridlines.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
