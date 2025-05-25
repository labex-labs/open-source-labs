# 사용자 정의 삼각 분할 생성

이 단계에서는 사용자 정의 삼각 분할 (triangulation) 을 생성하고 원치 않는 삼각형을 마스크 처리합니다.

```python
triang = tri.Triangulation(x, y)
triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```
