# SkewSpineクラスを定義する

SkewSpineクラスは、上のX軸の別個のデータ範囲を計算し、そこにスパインを描画します。また、この範囲をX軸のアーティストに提供して、目盛りと目盛り目安を表示します。

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
