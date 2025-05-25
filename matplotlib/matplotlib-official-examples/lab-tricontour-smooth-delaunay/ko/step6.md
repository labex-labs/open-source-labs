# 삼각 측량 개선

`TriAnalyzer`를 사용하여 삼각 측량의 경계에서 모양이 좋지 않은 (평평한) 삼각형을 제거하여 삼각 측량을 개선합니다. 그런 다음 `set_mask`를 사용하여 삼각 측량에 마스크를 적용합니다.

```python
# masking badly shaped triangles at the border of the triangular mesh.
mask = TriAnalyzer(tri).get_flat_tri_mask(min_circle_ratio)
tri.set_mask(mask)
```
