# 정점 및 코드 생성

복합 경로로 결합하려는 두 개의 다각형에 대한 정점 (vertices) 과 코드 (codes) 를 생성합니다. `Path.MOVETO`를 사용하여 커서를 다각형의 시작점으로 이동하고, `Path.LINETO`를 사용하여 시작점에서 다음 점까지 선을 만들고, `Path.CLOSEPOLY`를 사용하여 다각형을 닫습니다.

```python
vertices = []
codes = []

# First Polygon - Rectangle
codes = [Path.MOVETO] + [Path.LINETO]*3 + [Path.CLOSEPOLY]
vertices = [(1, 1), (1, 2), (2, 2), (2, 1), (0, 0)]

# Second Polygon - Triangle
codes += [Path.MOVETO] + [Path.LINETO]*2 + [Path.CLOSEPOLY]
vertices += [(4, 4), (5, 5), (5, 4), (0, 0)]
```
