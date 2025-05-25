# 삼각 분할 생성

`matplotlib.tri.Triangulation`을 사용하여 삼각 분할을 생성합니다. 삼각형을 지정할 필요가 없으므로, 점들의 Delaunay 삼각 분할이 자동으로 생성됩니다.

```python
triang = tri.Triangulation(x, y)
```
