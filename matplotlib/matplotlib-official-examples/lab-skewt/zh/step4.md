# 定义 SkewSpine 类

SkewSpine 类计算上 X 轴的单独数据范围，并在那里绘制脊柱（脊线）。它还将此范围提供给 X 轴艺术家以进行刻度和网格线设置。

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
