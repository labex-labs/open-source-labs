# PathPatch 객체 생성

이제 `Path` 객체를 갖게 되었으므로, 플롯에 베지어 곡선 (Bezier Curve) 을 그리는 데 사용될 `PathPatch` 객체를 생성할 수 있습니다. 곡선만 그려지고 채워지지 않도록 `facecolor`를 `'none'`으로 설정합니다.

```python
bezier_patch = mpatches.PathPatch(bezier_path, fc="none")
```
