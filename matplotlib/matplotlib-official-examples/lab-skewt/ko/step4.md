# SkewSpine 클래스 정의

SkewSpine 클래스는 위쪽 X 축의 개별 데이터 범위를 계산하고 거기에 스파인을 그립니다. 또한 이 범위를 눈금 및 그리드 선을 위해 X 축 아티스트에게 제공합니다.

```python
class SkewSpine(mspines.Spine):
    def _adjust_location(self):
        pts = self._path.vertices
        if self.spine_type == 'top':
            pts[:, 0] = self.axes.upper_xlim
        else:
            pts[:, 0] = self.axes.lower_xlim
```
