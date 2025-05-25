# Delaunay 삼각 측량 수행

`matplotlib.tri` 모듈의 `Triangulation` 함수를 사용하여 테스트 데이터 포인트에 대한 Delaunay 삼각 측량 (Delaunay triangulation) 을 수행합니다.

```python
# meshing with Delaunay triangulation
tri = Triangulation(x_test, y_test)
ntri = tri.triangles.shape[0]
```
