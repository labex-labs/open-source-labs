# 원치 않는 삼각형 마스크 처리

각 삼각형의 꼭지점 (vertices) 의 x 및 y 좌표의 평균을 계산하고 최소 반경 (minimum radius) 과 비교하여 원치 않는 삼각형을 마스크 처리합니다.

```python
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
