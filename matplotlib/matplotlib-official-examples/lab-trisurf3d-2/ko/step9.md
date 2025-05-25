# 원치 않는 삼각형 마스크 처리

각 삼각형의 중간점을 계산하고 주어진 반경 내에 속하는지 확인하여 원치 않는 삼각형을 마스크 처리합니다.

```python
xmid = x[triang.triangles].mean(axis=1)
ymid = y[triang.triangles].mean(axis=1)
mask = xmid**2 + ymid**2 < min_radius**2
triang.set_mask(mask)
```
