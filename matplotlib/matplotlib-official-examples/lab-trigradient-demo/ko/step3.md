# 삼각 측량 생성

```python
triang = Triangulation(x, y)

triang.set_mask(np.hypot(x[triang.triangles].mean(axis=1),
                         y[triang.triangles].mean(axis=1))
                < min_radius)
```

설명:

- `Triangulation`은 점 집합으로부터 Delaunay 삼각 측량 (Delaunay triangulation) 을 생성하는 클래스입니다.
- `triang`은 `Triangulation` 클래스의 인스턴스입니다.
- `triang.set_mask`는 원치 않는 삼각형을 마스크 처리합니다.
